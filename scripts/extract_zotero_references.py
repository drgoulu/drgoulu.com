#!/usr/bin/env python3
"""
extract_zotero_references.py
Extracts all bibliographic references from drgoulu.com Hugo posts and creates
importable Zotero files (.bib and .ris) with L4 links to corresponding blog posts.
"""

import os
import re
import sys
import json
import time
import glob
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    sys.exit(1)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
POSTS_DIR = os.path.join(BASE_DIR, 'content')
CACHE_FILE = os.path.join(BASE_DIR, '.ref_cache.json')
BIB_OUTPUT = os.path.join(BASE_DIR, 'drgoulu_references.bib')
RIS_OUTPUT = os.path.join(BASE_DIR, 'drgoulu_references.ris')

HEADERS = {
    'User-Agent': 'DrGouluReferenceExtractor/1.0 (https://drgoulu.com; mailto:goulu@drgoulu.com)'
}

# Regexes
FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
OPENBOOK_RE = re.compile(r'\{\{<\s*openbook\s+([^>]+)>\}\}|\[openbook\s+([^\]]+)\]', re.IGNORECASE)
ALTMETRIC_RE = re.compile(r'\{\{<\s*altmetric\s+([^>]+)>\}\}|\[altmetric\s+([^\]]+)\]', re.IGNORECASE)
DOI_RE = re.compile(r'\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', re.IGNORECASE)
ARXIV_RE = re.compile(r'(?:arxiv\.org/(?:abs|pdf)/|arxiv:\s*)([0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?|[a-z\-]+(?:\.[A-Z]{2})?/[0-9]{7})', re.IGNORECASE)
ISBN_RE = re.compile(r'(?:ISBN(?:-1[03])?:?\s*)?((?:97[89][-\s]?)?[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9X])\b', re.IGNORECASE)
HEADER_REF_RE = re.compile(r'^(#{1,4}\s*(?:R[ée]f[ée]rences?|References?|Sources?|Bibliographie)[^\n]*)', re.IGNORECASE | re.MULTILINE)
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(\s*(https?://[^\s"\'\)]+)(?:\s+["\'][^"\']*["\'])?\s*\)')
RAW_URL_RE = re.compile(r'https?://[^\s"\'\)\]>]+', re.IGNORECASE)
HTML_TAG_RE = re.compile(r'<[^>]+>')


def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning loading cache: {e}")
    return {}


def save_cache(cache):
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Warning saving cache: {e}")


def clean_text(text):
    text = HTML_TAG_RE.sub('', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&quot;', '"')
    return re.sub(r'\s+', ' ', text).strip()


def unwrap_url(url):
    if not url:
        return ""
    # Unwrap Google redirect URLs
    m = re.search(r'[?&]q=([^&]+)', url)
    if m:
        target = urllib.parse.unquote(m.group(1))
        if target.startswith('http'):
            return target
    return url


def clean_markdown_formatting(text):
    if not text:
        return ""
    # Convert [Title](url) to Title
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove markdown italics/bolds _text_ or *text*
    text = re.sub(r'(?:^|[\s(])[_*]{1,2}(.*?)[_*]{1,2}(?:[\s).,;:]|$)', r' \1 ', text)
    text = text.replace('_', ' ').replace('*', ' ')
    # Clean redundant whitespace and quotes
    text = re.sub(r'\s+', ' ', text).strip(' "\'«»“”')
    return text


def clean_author(auth):
    if not auth:
        return ""
    auth = clean_text(auth)
    auth = re.sub(r'[{}\[\]\(\)]', '', auth).strip(' ,-–_:')
    if auth.lower().startswith('doi=') or 'altmetric' in auth.lower() or 'openbook' in auth.lower():
        return ""
    return auth


def parse_bibtex_entry(bib):
    fields = {}
    pattern = re.compile(r'([a-zA-Z_-]+)\s*=\s*(?:\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}|\"([^\"]*)\"|([a-zA-Z0-9_-]+))')
    for m in pattern.finditer(bib):
        key = m.group(1).lower()
        val = m.group(2) if m.group(2) is not None else (m.group(3) if m.group(3) is not None else m.group(4))
        if val:
            fields[key] = val.strip()
    return fields


def clean_doi(doi):
    doi = doi.strip()
    # Remove URL prefixes
    doi = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', doi, flags=re.IGNORECASE)
    doi = re.sub(r'^doi:\s*', '', doi, flags=re.IGNORECASE)
    # Remove publisher prefixes if embedded in URL
    doi = re.sub(r'^.*?/doi/(?:abs/|full/|pdf/)?', '', doi)
    # Strip trailing punctuation and brackets first
    doi = re.sub(r'[\.,;:\)\]>_"\']+$', '', doi)
    # Strip trailing URL endpoints like /abstract, /full, /pdf
    doi = re.sub(r'/(?:abstract|full|pdf)$', '', doi, flags=re.IGNORECASE)
    # Strip trailing punctuation again if revealed
    doi = re.sub(r'[\.,;:\)\]>_"\']+$', '', doi)
    return doi.strip()


def clean_isbn(raw):
    clean = re.sub(r'[^0-9X]', '', raw.upper())
    if len(clean) in (10, 13):
        return clean
    return None


def get_post_metadata(content, filepath):
    fname = os.path.basename(filepath)
    fm = FRONTMATTER_RE.match(content)
    fm_text = fm.group(1) if fm else ""
    
    title = os.path.splitext(fname)[0]
    date_str = ""
    slug = ""
    
    if fm_text:
        t_m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if t_m:
            title = t_m.group(1).strip()
        d_m = re.search(r'^date:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if d_m:
            date_str = d_m.group(1).strip()[:10]
        s_m = re.search(r'^slug:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if s_m:
            slug = s_m.group(1).strip()
        u_m = re.search(r'^url:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
        if u_m and u_m.group(1).strip():
            u = u_m.group(1).strip()
            if not u.startswith("http"):
                u = "https://drgoulu.com" + ("/" if not u.startswith("/") else "") + u
            return title, date_str, u.rstrip("/") + "/"

    if "/pages/" in filepath:
        s = slug or os.path.splitext(fname)[0]
        return title, date_str, f"https://drgoulu.com/{s}/"

    fn_m = re.match(r'^(\d{4})-(\d{2})-(\d{2})-(.*)\.md$', fname)
    if fn_m:
        y, m, d, fn_slug = fn_m.groups()
        s = slug or fn_slug
        post_url = f"https://drgoulu.com/{y}/{m}/{d}/{s}/"
    elif date_str and len(date_str) == 10:
        y, m, d = date_str.split("-")
        s = slug or os.path.splitext(fname)[0]
        post_url = f"https://drgoulu.com/{y}/{m}/{d}/{s}/"
    else:
        s = slug or os.path.splitext(fname)[0]
        post_url = f"https://drgoulu.com/{s}/"

    return title, date_str, post_url


class ReferenceCollection:
    def __init__(self):
        self.refs = {}  # key -> dict

    def add_reference(self, key, ref_type, identifier, post_url, raw_text="", metadata=None):
        if not key:
            return
        if key not in self.refs:
            self.refs[key] = {
                'key': key,
                'type': ref_type,
                'identifier': identifier,
                'post_urls': set(),
                'raw_texts': set(),
                'metadata': metadata or {}
            }
        if post_url:
            self.refs[key]['post_urls'].add(post_url)
        if raw_text:
            clean_raw = clean_text(raw_text)
            if clean_raw:
                self.refs[key]['raw_texts'].add(clean_raw)
        if metadata:
            self.refs[key]['metadata'].update(metadata)


def extract_from_posts():
    collection = ReferenceCollection()
    md_files = glob.glob(os.path.join(POSTS_DIR, '**/*.md'), recursive=True)
    print(f"Scanning {len(md_files)} markdown files...")

    for fpath in md_files:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        post_title, post_date, post_url = get_post_metadata(content, fpath)

        # 1. OpenBook Shortcodes
        for m in OPENBOOK_RE.finditer(content):
            raw_arg = (m.group(1) or m.group(2)).strip()
            bn_match = re.search(r'booknumber=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
            arg = bn_match.group(1) if bn_match else raw_arg.split()[0].strip('\"\'')
            
            if 'OLID:' in arg.upper() or arg.upper().startswith('OL'):
                olid = re.sub(r'^OLID:', '', arg, flags=re.IGNORECASE).strip()
                collection.add_reference(f"olid:{olid}", "olid", olid, post_url, raw_arg)
            elif 'ISBN:' in arg.upper() or re.match(r'^[0-9X-]+$', arg):
                isbn = clean_isbn(arg)
                if isbn:
                    collection.add_reference(f"isbn:{isbn}", "isbn", isbn, post_url, raw_arg)

        # 2. Altmetric Shortcodes
        for m in ALTMETRIC_RE.finditer(content):
            raw_arg = (m.group(1) or m.group(2)).strip()
            doi_m = re.search(r'doi=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
            if doi_m:
                doi = clean_doi(doi_m.group(1))
                collection.add_reference(f"doi:{doi.lower()}", "doi", doi, post_url, raw_arg)
            
            arx_m = re.search(r'arxiv(?:_id)?=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
            if arx_m:
                arx = arx_m.group(1).strip()
                collection.add_reference(f"arxiv:{arx.lower()}", "arxiv", arx, post_url, raw_arg)

            isbn_m = re.search(r'isbn=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
            if isbn_m:
                isbn = clean_isbn(isbn_m.group(1))
                if isbn:
                    collection.add_reference(f"isbn:{isbn}", "isbn", isbn, post_url, raw_arg)

            first_arg = raw_arg.split()[0].strip('\"\'')
            if first_arg.startswith('10.'):
                doi = clean_doi(first_arg)
                collection.add_reference(f"doi:{doi.lower()}", "doi", doi, post_url, raw_arg)
            elif re.match(r'^[0-9]{4}\.[0-9]{4,5}', first_arg):
                collection.add_reference(f"arxiv:{first_arg.lower()}", "arxiv", first_arg, post_url, raw_arg)

        # 3. Raw DOIs in content
        for d in DOI_RE.findall(content):
            doi = clean_doi(d)
            if len(doi) > 7 and '/' in doi:
                collection.add_reference(f"doi:{doi.lower()}", "doi", doi, post_url)

        # 4. Raw arXiv in content
        for arx in ARXIV_RE.findall(content):
            clean_arx = arx.strip().rstrip('.,;')
            collection.add_reference(f"arxiv:{clean_arx.lower()}", "arxiv", clean_arx, post_url)

        # 5. Références / Sources / Bibliographie sections
        for h_m in HEADER_REF_RE.finditer(content):
            start = h_m.end()
            next_h = re.search(r'^(#{1,4}\s+[^\n]+)', content[start:], re.MULTILINE)
            end = start + next_h.start() if next_h else len(content)
            sec_text = content[start:end].strip()

            lines = [l.strip() for l in sec_text.split('\n') if l.strip()]
            for line in lines:
                if not re.match(r'^(?:\d+[\.\)]|[-*+])\s+', line):
                    continue
                item_text = re.sub(r'^(?:\d+[\.\)]|[-*+])\s+', '', line).strip()
                item_clean = clean_text(item_text)
                if not item_clean or len(item_clean) < 5:
                    continue

                # Check OpenBook shortcodes
                ob_m = OPENBOOK_RE.search(item_text)
                if ob_m:
                    raw_arg = (ob_m.group(1) or ob_m.group(2)).strip()
                    bn_m = re.search(r'booknumber=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
                    arg = bn_m.group(1) if bn_m else raw_arg.split()[0].strip('\"\'')
                    if 'OLID:' in arg.upper() or arg.upper().startswith('OL'):
                        olid = re.sub(r'^OLID:', '', arg, flags=re.IGNORECASE).strip()
                        collection.add_reference(f"olid:{olid}", "olid", olid, post_url, item_clean)
                        continue
                    isbn = clean_isbn(arg)
                    if isbn:
                        collection.add_reference(f"isbn:{isbn}", "isbn", isbn, post_url, item_clean)
                        continue

                # Check Altmetric shortcodes
                am_m = ALTMETRIC_RE.search(item_text)
                if am_m:
                    raw_arg = (am_m.group(1) or am_m.group(2)).strip()
                    doi_m = re.search(r'doi=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
                    if doi_m:
                        doi = clean_doi(doi_m.group(1))
                        collection.add_reference(f"doi:{doi.lower()}", "doi", doi, post_url, item_text)
                        continue
                    arx_m = re.search(r'arxiv(?:_id)?=["\']?([^"\'\s]+)', raw_arg, re.IGNORECASE)
                    if arx_m:
                        arx = arx_m.group(1).strip()
                        collection.add_reference(f"arxiv:{arx.lower()}", "arxiv", arx, post_url, item_text)
                        continue
                    first_arg = raw_arg.split()[0].strip('\"\'')
                    if first_arg.startswith('10.'):
                        doi = clean_doi(first_arg)
                        collection.add_reference(f"doi:{doi.lower()}", "doi", doi, post_url, item_text)
                        continue

                # Check DOI in item_text
                d_match = DOI_RE.search(item_text)
                if d_match:
                    doi = clean_doi(d_match.group(0))
                    collection.add_reference(f"doi:{doi.lower()}", "doi", doi, post_url, item_text)
                    continue

                # Check arXiv
                arx_m = ARXIV_RE.search(item_text)
                if arx_m:
                    arx = arx_m.group(1).strip()
                    collection.add_reference(f"arxiv:{arx.lower()}", "arxiv", arx, post_url, item_clean)
                    continue

                # Check ISBN
                isbn_m = ISBN_RE.search(item_clean)
                if isbn_m:
                    isbn = clean_isbn(isbn_m.group(1))
                    if isbn:
                        collection.add_reference(f"isbn:{isbn}", "isbn", isbn, post_url, item_clean)
                        continue

                # Check markdown links
                links = MD_LINK_RE.findall(item_text)
                raw_urls = RAW_URL_RE.findall(item_text)

                if links or raw_urls:
                    if links:
                        link_anchor, link_url = links[0]
                    else:
                        link_url = raw_urls[0]
                        link_anchor = ""

                    norm_url = unwrap_url(urllib.parse.urldefrag(link_url)[0].strip())
                    norm_url = re.sub(r'([?&])utm_[^&]+(&|$)', r'\1', norm_url).rstrip('?&')

                    # Extract site / blog name from "sur <Site>" or domain
                    site = ""
                    site_m = re.search(r'\bsur\s+([a-zA-Z0-9_\-\. ]+?)(?:[\(\[\n]|$)', item_clean)
                    if site_m:
                        site = clean_markdown_formatting(site_m.group(1))
                    elif 'discovermagazine.com/badastronomy' in norm_url:
                        site = 'BadAstronomy'
                    elif 'wikipedia.org' in norm_url:
                        site = 'Wikipédia'

                    # Extract year
                    year_m = re.search(r'\b(19\d\d|20\d\d)\b', item_clean)
                    if not year_m:
                        year_m = re.search(r'/((?:19|20)\d\d)/', norm_url)
                    year = year_m.group(1) if year_m else (post_date[:4] if post_date else "")

                    # Extract author and title
                    author = ""
                    quote_m = re.search(r'["«“]([^"»”]+)["»”]', item_text)
                    if quote_m:
                        raw_title = quote_m.group(1)
                        title = clean_markdown_formatting(raw_title)
                        prefix = item_text[:quote_m.start()].strip(' ,-–_:')
                        prefix = re.sub(r'\([^\)]*\)', '', prefix).strip(' ,-–_:')
                        prefix_clean = clean_markdown_formatting(prefix)
                        if len(prefix_clean) > 2 and not prefix_clean.lower().startswith('http'):
                            author = prefix_clean
                    elif link_anchor:
                        title = clean_markdown_formatting(link_anchor)
                    else:
                        title = clean_markdown_formatting(item_clean[:100])

                    key = f"url:{norm_url}"
                    collection.add_reference(key, "web", norm_url, post_url, item_clean, metadata={
                        'title': title,
                        'author': author,
                        'site': site,
                        'year': year,
                        'url': norm_url
                    })
                    continue

                # Plain textual citation without URL or ID
                norm_text = re.sub(r'\s+', ' ', item_clean)
                text_key = "text:" + re.sub(r'[^a-zA-Z0-9]', '', norm_text[:60]).lower()
                collection.add_reference(text_key, "text", norm_text, post_url, item_clean)

    return collection


def fetch_doi_metadata(doi, cache):
    cache_key = f"doi:{doi.lower()}"
    cached = cache.get(cache_key)

    # If already cached with full fields, return it
    if cached and cached.get('title') and cached.get('author') and cached.get('journal'):
        return cached

    # If cached has bibtex, parse it!
    if cached and cached.get('bibtex'):
        p = parse_bibtex_entry(cached['bibtex'])
        if p.get('title'):
            cached.update({
                'title': p.get('title', ''),
                'author': p.get('author', ''),
                'journal': p.get('journal', ''),
                'year': p.get('year', ''),
                'volume': p.get('volume', ''),
                'issue': p.get('number') or p.get('issue', ''),
                'pages': p.get('pages', ''),
                'publisher': p.get('publisher', ''),
                'url': p.get('url') or f"https://doi.org/{doi}",
                'doi': doi
            })
            cache[cache_key] = cached
            return cached

    res = {'doi': doi}
    # 1. Query CrossRef Works API
    try:
        cr_url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
        cr_resp = requests.get(cr_url, headers=HEADERS, timeout=8)
        if cr_resp.status_code == 200:
            data = cr_resp.json().get('message', {})
            title = " ".join(data.get('title', []))
            authors = []
            for a in data.get('author', []):
                given = a.get('given', '')
                family = a.get('family', '')
                if family and given:
                    authors.append(f"{family}, {given}")
                elif family:
                    authors.append(family)
            journal = " ".join(data.get('container-title', []))
            year = ""
            issued = data.get('issued', {}).get('date-parts', [[]])[0]
            if issued:
                year = str(issued[0])
            res.update({
                'title': title,
                'author': " and ".join(authors),
                'journal': journal,
                'year': year,
                'doi': doi,
                'publisher': data.get('publisher', ''),
                'volume': str(data.get('volume', '')),
                'issue': str(data.get('issue', '')),
                'pages': str(data.get('page', '')),
                'url': data.get('URL') or f"https://doi.org/{doi}"
            })
    except Exception:
        pass

    # 2. Query CrossRef BibTeX
    try:
        url = f"https://doi.org/{urllib.parse.quote(doi)}"
        headers = dict(HEADERS)
        headers['Accept'] = 'application/x-bibtex; charset=utf-8'
        resp = requests.get(url, headers=headers, timeout=8, allow_redirects=True)
        if resp.status_code == 200 and '@' in resp.text:
            res['bibtex'] = resp.text.strip()
            p = parse_bibtex_entry(res['bibtex'])
            for k in ('title', 'author', 'journal', 'year', 'volume', 'pages', 'publisher'):
                if not res.get(k) and p.get(k):
                    res[k] = p[k]
            if not res.get('issue') and (p.get('number') or p.get('issue')):
                res['issue'] = p.get('number') or p.get('issue')
    except Exception:
        pass

    if res.get('title') or res.get('bibtex'):
        cache[cache_key] = res
        return res

    cache[cache_key] = None
    return None


def fetch_openlibrary_metadata(key_type, value, cache):
    cache_key = f"{key_type}:{value}"
    if cache_key in cache and cache[cache_key]:
        return cache[cache_key]

    bibkey = f"ISBN:{value}" if key_type == 'isbn' else f"OLID:{value}"
    url = f"https://openlibrary.org/api/books?bibkeys={bibkey}&format=json&jscmd=data"
    
    for attempt in range(2):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=8)
            if resp.status_code == 200:
                data = resp.json().get(bibkey)
                if data:
                    title = data.get('title', '')
                    if data.get('subtitle'):
                        title += f": {data['subtitle']}"
                    authors = [a.get('name') for a in data.get('authors', []) if a.get('name')]
                    publishers = [p.get('name') for p in data.get('publishers', []) if p.get('name')]
                    pub_date = data.get('publish_date', '')
                    year_match = re.search(r'\b(19\d\d|20\d\d)\b', pub_date)
                    year = year_match.group(1) if year_match else pub_date
                    res = {
                        'title': title,
                        'author': " and ".join(authors),
                        'publisher': ", ".join(publishers),
                        'year': year,
                        'url': data.get('url', ''),
                        'pages': str(data.get('number_of_pages', '')) if data.get('number_of_pages') else '',
                        key_type: value
                    }
                    cache[cache_key] = res
                    return res
                else:
                    break
        except Exception:
            time.sleep(0.5)

    cache[cache_key] = None
    return None


def fetch_arxiv_metadata(arx_id, cache):
    cache_key = f"arxiv:{arx_id.lower()}"
    if cache_key in cache and cache[cache_key]:
        return cache[cache_key]

    url = f"https://export.arxiv.org/api/query?search_query=id:{urllib.parse.quote(arx_id)}&max_results=1"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=8)
        if resp.status_code == 200 and '<entry>' in resp.text:
            root = ET.fromstring(resp.text)
            entry = root.find('{http://www.w3.org/2005/Atom}entry')
            if entry is not None:
                title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
                title = clean_text(title_elem.text) if title_elem is not None else ""
                authors = []
                for a in entry.findall('{http://www.w3.org/2005/Atom}author'):
                    n = a.find('{http://www.w3.org/2005/Atom}name')
                    if n is not None and n.text:
                        authors.append(n.text.strip())
                pub_elem = entry.find('{http://www.w3.org/2005/Atom}published')
                year = pub_elem.text[:4] if pub_elem is not None and pub_elem.text else ""
                cat_elem = entry.find('{http://arxiv.org/schemas/atom}primary_category')
                primary_class = cat_elem.attrib.get('term', '') if cat_elem is not None else ''
                res = {
                    'title': title,
                    'author': " and ".join(authors),
                    'year': year,
                    'eprint': arx_id,
                    'archivePrefix': 'arXiv',
                    'primaryClass': primary_class,
                    'url': f"https://arxiv.org/abs/{arx_id}"
                }
                cache[cache_key] = res
                return res
    except Exception:
        pass

    cache[cache_key] = None
    return None


def parse_text_citation(text):
    res = {'raw': text}
    year_m = re.search(r'\b(19\d\d|20\d\d)\b', text)
    if year_m:
        res['year'] = year_m.group(1)

    title_m = re.search(r'["«“]([^"»”]+)["»”]', text)
    if title_m:
        res['title'] = clean_markdown_formatting(title_m.group(1))
        prefix = text[:title_m.start()].strip()
        author_clean = re.sub(r'\(\s*(?:19|20)\d\d\s*\)', '', prefix)
        author_clean = re.sub(r'[()\[\]]', '', author_clean).strip(' ,-–_:')
        if author_clean and len(author_clean) > 2:
            res['author'] = author_clean
        suffix = text[title_m.end():].strip()
        suffix = re.sub(r'^(?:in\s*|,\s*|_\s*)+', '', suffix)
        suffix_clean = clean_markdown_formatting(suffix)
        if suffix_clean:
            res['journal'] = suffix_clean
    else:
        link_m = re.search(r'\[([^\]]+)\]\((https?://[^\s\)]+)\)', text)
        if link_m:
            res['title'] = clean_markdown_formatting(link_m.group(1))
            res['url'] = unwrap_url(link_m.group(2))
        else:
            res['title'] = clean_markdown_formatting(text[:100])

    return res


def enrich_references(collection, cache):
    print("Enriching metadata via APIs (CrossRef, OpenLibrary, arXiv)...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {}
        for key, ref in collection.refs.items():
            t = ref['type']
            ident = ref['identifier']
            if t == 'doi':
                futures[executor.submit(fetch_doi_metadata, ident, cache)] = key
            elif t in ('isbn', 'olid'):
                futures[executor.submit(fetch_openlibrary_metadata, t, ident, cache)] = key
            elif t == 'arxiv':
                futures[executor.submit(fetch_arxiv_metadata, ident, cache)] = key

        done_count = 0
        total = len(futures)
        for f in as_completed(futures):
            key = futures[f]
            done_count += 1
            if done_count % 20 == 0 or done_count == total:
                print(f"  API progress: {done_count}/{total} resolved")
            try:
                meta = f.result()
                if meta:
                    collection.refs[key]['metadata'].update(meta)
            except Exception:
                pass

    save_cache(cache)


def make_bibtex_key(ref, idx):
    meta = ref.get('metadata', {})
    auth = meta.get('author') or ""
    first_author = re.split(r'[, ]+', auth)[0].lower() if auth else ""
    first_author = re.sub(r'[^a-z]', '', first_author)
    year = meta.get('year') or ""
    t = ref['type']
    ident = re.sub(r'[^a-zA-Z0-9]', '', ref.get('identifier', ''))[:15]

    if first_author and year:
        return f"{first_author}_{year}_{idx}"
    elif t == 'doi' and ident:
        return f"doi_{ident}_{idx}"
    elif t == 'isbn' and ident:
        return f"isbn_{ident}_{idx}"
    elif t == 'arxiv' and ident:
        return f"arxiv_{ident}_{idx}"
    else:
        return f"ref_drgoulu_{idx}"


def sanitize_bibtex_val(val):
    if not val:
        return ""
    val = str(val).strip()
    val = val.replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')
    return val


def generate_bibtex_and_ris(collection):
    bib_entries = []
    ris_entries = []

    print(f"Generating BibTeX and RIS files for {len(collection.refs)} unique references...")

    for idx, (key, ref) in enumerate(collection.refs.items(), start=1):
        meta = ref.get('metadata', {})
        t = ref.get('type')
        post_urls = sorted(ref.get('post_urls', set()))
        citing_tags = "blog-drgoulu"

        # Check if raw text needs parsing
        if not meta.get('title') and ref['raw_texts']:
            for raw_t in ref['raw_texts']:
                parsed = parse_text_citation(raw_t)
                for k, v in parsed.items():
                    if k not in meta and v:
                        meta[k] = v
                if meta.get('title'):
                    break

        # File attachments link for BibTeX
        file_field_val = ";".join([f"Article Dr Goulu:{u}:text/html" for u in post_urls])
        urls_str = " ; ".join(post_urls)

        # 1. BibTeX generation
        if 'bibtex' in meta and meta['bibtex']:
            raw_bib = meta['bibtex'].strip()
            # Remove any previous note or howpublished field if present
            raw_bib = re.sub(r',\s*note\s*=\s*\{[^}]*\}', '', raw_bib)
            raw_bib = re.sub(r',\s*howpublished\s*=\s*\{[^}]*\}', '', raw_bib)
            fields_to_inject = []
            if file_field_val:
                fields_to_inject.append(f"  file = {{{file_field_val}}}")
            if post_urls:
                fields_to_inject.append(f"  howpublished = {{\\url{{{post_urls[0]}}}}}")
                fields_to_inject.append(f"  note = {{Cité sur Dr Goulu : \\url{{{urls_str}}}}}")
            fields_to_inject.append(f"  keywords = {{{citing_tags}}}")
            injection = ",\n" + ",\n".join(fields_to_inject) + "\n}}"

            if raw_bib.endswith('}'):
                modified_bib = raw_bib[:-1].rstrip() + injection
            else:
                modified_bib = raw_bib + "\n" + injection
            bib_entries.append(modified_bib)
        else:
            cite_key = make_bibtex_key(ref, idx)
            entry_type = "misc"
            if t in ('isbn', 'olid'):
                entry_type = "book"
            elif t in ('doi', 'arxiv') or meta.get('journal'):
                entry_type = "article"
            elif t == 'web' or meta.get('url'):
                entry_type = "online"

            raw_title = meta.get('title') or (next(iter(ref['raw_texts']))[:150] if ref['raw_texts'] else ref['identifier'])
            clean_t = clean_markdown_formatting(raw_title)

            fields = [f"  title = {{{sanitize_bibtex_val(clean_t)}}}"]

            if meta.get('author'):
                fields.append(f"  author = {{{sanitize_bibtex_val(meta['author'])}}}")
            if meta.get('year'):
                fields.append(f"  year = {{{meta['year']}}}")
            if meta.get('journal'):
                fields.append(f"  journal = {{{sanitize_bibtex_val(clean_markdown_formatting(meta['journal']))}}}")
            if meta.get('site'):
                fields.append(f"  organization = {{{sanitize_bibtex_val(meta['site'])}}}")
            if meta.get('publisher'):
                fields.append(f"  publisher = {{{sanitize_bibtex_val(meta['publisher'])}}}")
            if meta.get('volume'):
                fields.append(f"  volume = {{{sanitize_bibtex_val(meta['volume'])}}}")
            if meta.get('issue'):
                fields.append(f"  number = {{{sanitize_bibtex_val(meta['issue'])}}}")
            if meta.get('pages'):
                fields.append(f"  pages = {{{sanitize_bibtex_val(meta['pages'])}}}")
            if meta.get('doi') or (t == 'doi'):
                fields.append(f"  doi = {{{meta.get('doi', ref.get('identifier'))}}}")
            if meta.get('isbn') or (t == 'isbn'):
                fields.append(f"  isbn = {{{meta.get('isbn', ref.get('identifier'))}}}")
            if meta.get('eprint'):
                fields.append(f"  eprint = {{{meta['eprint']}}}")
                fields.append(f"  archivePrefix = {{{meta.get('archivePrefix', 'arXiv')}}}")
            
            clean_u = unwrap_url(meta.get('url', ''))
            if clean_u:
                fields.append(f"  url = {{{clean_u}}}")
            elif t == 'doi':
                fields.append(f"  url = {{https://doi.org/{ref['identifier']}}}")
            elif t == 'arxiv':
                fields.append(f"  url = {{https://arxiv.org/abs/{ref['identifier']}}}")

            if file_field_val:
                fields.append(f"  file = {{{file_field_val}}}")
            if post_urls:
                if entry_type == "online" and not clean_u:
                    fields.append(f"  howpublished = {{\\url{{{post_urls[0]}}}}}")
                fields.append(f"  note = {{Cité sur Dr Goulu : \\url{{{urls_str}}}}}")
            fields.append(f"  keywords = {{{citing_tags}}}")

            bib_entries.append(f"@{entry_type}{{{cite_key},\n" + ",\n".join(fields) + "\n}")

        # 2. RIS generation
        ris_lines = []
        if t in ('isbn', 'olid'):
            ris_lines.append("TY  - BOOK")
        elif t in ('doi', 'arxiv') or meta.get('journal'):
            ris_lines.append("TY  - JOUR")
        else:
            ris_lines.append("TY  - ELEC")

        raw_title = meta.get('title')
        if not raw_title and ref['raw_texts']:
            for raw_t in ref['raw_texts']:
                parsed = parse_text_citation(raw_t)
                if parsed.get('title') and not parsed['title'].startswith('10.'):
                    raw_title = parsed['title']
                    break
        if not raw_title:
            raw_title = ref['identifier']
        ris_lines.append(f"TI  - {clean_markdown_formatting(raw_title)}")

        authors = meta.get('author')
        if not authors and ref['raw_texts']:
            for raw_t in ref['raw_texts']:
                parsed = parse_text_citation(raw_t)
                if parsed.get('author'):
                    authors = parsed['author']
                    break
        if authors:
            for auth in re.split(r'\s+and\s+', authors):
                clean_a = clean_author(auth)
                if clean_a:
                    ris_lines.append(f"AU  - {clean_a}")

        journal = meta.get('journal')
        if not journal and ref['raw_texts']:
            for raw_t in ref['raw_texts']:
                parsed = parse_text_citation(raw_t)
                if parsed.get('journal'):
                    journal = parsed['journal']
                    break
        if journal:
            ris_lines.append(f"JO  - {clean_markdown_formatting(journal)}")
        elif meta.get('site'):
            ris_lines.append(f"T2  - {meta['site']}")

        year = meta.get('year')
        if not year and ref['raw_texts']:
            for raw_t in ref['raw_texts']:
                parsed = parse_text_citation(raw_t)
                if parsed.get('year'):
                    year = parsed['year']
                    break
        if year:
            ris_lines.append(f"DA  - {year}///")
            ris_lines.append(f"PY  - {year}")

        if meta.get('publisher'):
            ris_lines.append(f"PB  - {clean_text(meta['publisher'])}")
        if meta.get('volume'):
            ris_lines.append(f"VL  - {meta['volume']}")
        if meta.get('issue'):
            ris_lines.append(f"IS  - {meta['issue']}")
        if meta.get('pages'):
            ris_lines.append(f"SP  - {meta['pages']}")
        if meta.get('doi') or (t == 'doi'):
            ris_lines.append(f"DO  - {meta.get('doi', ref.get('identifier'))}")
        if meta.get('isbn') or (t == 'isbn'):
            ris_lines.append(f"SN  - {meta.get('isbn', ref.get('identifier'))}")
        
        clean_u = unwrap_url(meta.get('url', ''))
        if clean_u:
            ris_lines.append(f"UR  - {clean_u}")
        elif t == 'doi':
            ris_lines.append(f"UR  - https://doi.org/{ref['identifier']}")
        elif t == 'arxiv':
            ris_lines.append(f"UR  - https://arxiv.org/abs/{ref['identifier']}")

        # L4 link to drgoulu.com article(s) - creates attached link in Zotero
        for post_u in post_urls:
            ris_lines.append(f"L4  - {post_u}")

        ris_lines.append(f"KW  - {citing_tags}")
        ris_lines.append("ER  - \n")

        ris_entries.append("\n".join(ris_lines))

    # Write files
    with open(BIB_OUTPUT, 'w', encoding='utf-8') as f:
        f.write("% Bibliographic references extracted from drgoulu.com\n")
        f.write(f"% Total entries: {len(bib_entries)}\n\n")
        f.write("\n\n".join(bib_entries) + "\n")

    with open(RIS_OUTPUT, 'w', encoding='utf-8') as f:
        f.write("\n".join(ris_entries) + "\n")

    print(f"Successfully generated:")
    print(f"  - {BIB_OUTPUT} ({len(bib_entries)} entries, {os.path.getsize(BIB_OUTPUT)} bytes)")
    print(f"  - {RIS_OUTPUT} ({len(ris_entries)} entries, {os.path.getsize(RIS_OUTPUT)} bytes)")


def main():
    start_time = time.time()
    cache = load_cache()
    collection = extract_from_posts()
    enrich_references(collection, cache)
    generate_bibtex_and_ris(collection)
    elapsed = time.time() - start_time
    print(f"\nDone in {elapsed:.1f}s.")


if __name__ == '__main__':
    main()
