#!/usr/bin/env python3
"""
export_pourlascience.py
Scrapes and exports all bibliographic references from Pour la Science index:
https://www.pourlascience.fr/statics/index-articles-pourlascience
into Zotero-compatible formats (.bib and .ris) in drgoulu.com.
"""

import os
import re
import sys
import html
import urllib.request
import unicodedata
from bs4 import BeautifulSoup

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BIB_OUTPUT = os.path.join(BASE_DIR, 'pourlascience.bib')
RIS_OUTPUT = os.path.join(BASE_DIR, 'pourlascience.ris')
SOURCE_URL = 'https://www.pourlascience.fr/statics/index-articles-pourlascience'
CACHE_HTML = os.path.join(BASE_DIR, '.pourlascience_cache.html')

MONTHS_FR = {
    'janvier': 1, 'fevrier': 2, 'février': 2, 'mars': 3, 'avril': 4, 'mai': 5, 'juin': 6,
    'juillet': 7, 'aout': 8, 'août': 8, 'septembre': 9, 'octobre': 10, 'novembre': 11,
    'decembre': 12, 'décembre': 12
}

MONTH_NAMES_FR = [
    "", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]

KNOWN_RUBRIQUES = {
    'archéologie', 'physique', 'physique théorique', 'astrophysique', 'technologie',
    'informatique', 'santé', 'biogéographie', 'biologie', 'biologie marine', 'biologie cellulaire',
    'sciences cognitives', 'sinologie', 'linguistique', 'paléontologie', 'géophysique',
    'mathématiques', 'éthologie', 'médecine', 'médecine légale', 'neurosciences',
    'point de vue', 'développement durable', 'vrai ou faux', 'histoire des sciences',
    'logique et calcul', 'logique & calcul', 'science et fiction', 'science & fiction',
    'art et science', 'art & science', 'idées de physique', 'science et gastronomie',
    'science & gastronomie', 'entretien', 'portfolio', 'économie', 'métrologie',
    'chimie', 'cosmologie', 'zoologie', 'biochimie', 'dossier', 'perspectives'
}


def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '_', text).strip('_')


def fix_encoding_artifacts(raw_html):
    # Fix corrupt ligatures in the source HTML
    replacements = [
        ('c?ur', 'cœur'), ('C?ur', 'Cœur'),
        ('?il', 'œil'), ('?ils', 'œils'),
        ('m?urs', 'mœurs'), ('n?ud', 'nœud'), ('n?uds', 'nœuds'),
        ('f?tus', 'fœtus'), ('Desc?udres', 'Descœudres'), ('L?uff', 'Lœuff'),
        ('février2012', 'février 2012'), ('février2013', 'février 2013'),
    ]
    for old, new in replacements:
        raw_html = raw_html.replace(old, new)
    # Separate month and year when glued together
    raw_html = re.sub(r'([a-zA-ZÀ-ÿ])(\d{4})', r'\1 \2', raw_html)
    return raw_html


def fetch_source_html():
    if os.path.exists(CACHE_HTML) and '--refresh' not in sys.argv:
        print(f"Loading cached HTML from {CACHE_HTML}...")
        with open(CACHE_HTML, 'r', encoding='utf-8') as f:
            return f.read()

    print(f"Fetching {SOURCE_URL}...")
    req = urllib.request.Request(SOURCE_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')

    with open(CACHE_HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved cache to {CACHE_HTML} ({len(content)} characters)")
    return content


def parse_h2(h2_elem):
    text = h2_elem.get_text(' ', strip=True)
    text = html.unescape(text)

    m_num = re.search(r'(?:N°|n°|\b)\s*(\d+)', text)
    issue_num = int(m_num.group(1)) if m_num else None

    m_year = re.search(r'\b(19\d\d|20\d\d)\b', text)
    year = int(m_year.group(1)) if m_year else None

    month = None
    for m_name, m_val in MONTHS_FR.items():
        if re.search(r'\b' + m_name + r'\b', text, re.IGNORECASE):
            month = m_val
            break

    # Fix known issues where date was omitted in header
    if issue_num == 436 and not year:
        year, month = 2014, 2
    elif issue_num == 437 and not year:
        year, month = 2014, 3

    # Extract issue theme / special title if any
    theme = ''
    parts = [p.strip() for p in re.split(r'\s*[-–—]\s*', text) if p.strip()]
    for p in parts:
        if not re.search(r'(?:Pour la Science|N°|n°|' + '|'.join(MONTHS_FR.keys()) + r'|\b19\d\d|\b20\d\d)', p, re.IGNORECASE):
            theme = p
            break

    return issue_num, year, month, theme, text


def split_authors(raw_auth):
    raw_auth = raw_auth.strip(' .;')
    norm = re.sub(r'\s+(?:et|and|&)\s+', ' # ', raw_auth)
    parts = re.split(r'[,#]\s*', norm)
    cleaned = []
    for p in parts:
        p = p.strip(' .')
        if p:
            cleaned.append(p)
    return cleaned


def parse_article_line(line, current_section, issue_theme):
    line = line.strip()
    if not line:
        return None, current_section

    # Check if section header
    if line.isupper() and len(line.split()) <= 6 and not line.startswith('-'):
        return None, line

    if re.match(r'^(?:<strong>)?\s*(Actualités|Perspectives scientifiques|DOSSIER[^\n:]*)\s*:?\s*(?:</strong>)?$', line, re.IGNORECASE):
        sec_name = re.sub(r'</?[^>]+>', '', line).strip(' :')
        return None, sec_name

    # Remove leading bullet dashes
    cleaned = re.sub(r'^[-–—•*]+\s*', '', line).strip()
    if not cleaned:
        return None, current_section

    # Check for rubric / category prefix in line (e.g., 'Archéologie : ...', 'Point de vue : ...')
    rubrique = ''
    m_rub = re.match(r'^([A-ZÀ-ÖØ-Ý][a-zà-öø-ÿA-ZÀ-ÖØ-Ý\s&]+?)\s*:\s*(.*)$', cleaned)
    if m_rub:
        prefix = m_rub.group(1).strip()
        rest = m_rub.group(2).strip()
        if len(prefix.split()) <= 4 and (prefix.lower() in KNOWN_RUBRIQUES or prefix.lower().startswith('dossier')):
            rubrique = prefix
            cleaned = rest

    # Skip isolated citation echoes
    if re.search(r'n°\s*\d+,\s*(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s*\d{4}', cleaned, re.IGNORECASE):
        return None, current_section

    # Parse title & authors
    title = ''
    authors = []

    # 1. Author in parentheses at the end: e.g. "Titre (Auteur)"
    m_paren = re.search(r'^(.*?)\s+\(([A-ZÀ-ÖØ-Ý][a-zA-ZÀ-ÿ\s,.\'-]+)\)\.?$', cleaned)
    if m_paren and not re.search(r'\d', m_paren.group(2)) and len(m_paren.group(2).split()) <= 6:
        title = m_paren.group(1).strip(' .')
        authors = split_authors(m_paren.group(2))
    else:
        # 2. "Titre, par Auteur" or "Titre par Auteur"
        m_par = list(re.finditer(r'(?:,\s*par|\s+par)\s+([A-ZÀ-ÖØ-Ý][a-zA-ZÀ-ÿ\s,.\'-]+)\.?$', cleaned))
        if m_par:
            last_m = m_par[-1]
            title = cleaned[:last_m.start()].strip(' ,;')
            authors = split_authors(last_m.group(1))
        else:
            # 3. "Titre, Auteur" where Auteur is 2-3 capitalized words
            m_author_comma = re.search(r'^(.*?),\s+([A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+(?:\s+(?:et|and)\s+[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+|\s+[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+){1,3})\.?$', cleaned)
            if m_author_comma and len(m_author_comma.group(1)) > 5:
                title = m_author_comma.group(1).strip()
                authors = split_authors(m_author_comma.group(2))
            else:
                title = cleaned.strip(' .')
                authors = []

    section = rubrique if rubrique else current_section
    return {
        'title': html.unescape(title),
        'authors': [html.unescape(a) for a in authors],
        'section': html.unescape(section) if section else '',
        'issue_theme': html.unescape(issue_theme) if issue_theme else ''
    }, current_section


def extract_articles_from_table(table, issue_theme):
    t_html = str(table)
    t_html = re.sub(r'([^\n])\s*([–—\-]\s*<strong)', r'\1\n\2', t_html, flags=re.IGNORECASE)
    t_html = re.sub(r'<br\s*/?>', '\n', t_html, flags=re.IGNORECASE)
    t_html = re.sub(r'</?(?:div|p|tr|td)[^>]*>', '\n', t_html, flags=re.IGNORECASE)

    s = BeautifulSoup(t_html, 'html.parser')
    text = s.get_text().replace('\xa0', ' ')
    raw_lines = [l.strip() for l in text.split('\n') if l.strip()]

    articles = []
    current_section = None

    for line in raw_lines:
        sublines = re.split(r'\.\s+[-–—]\s+', line)
        for i, subl in enumerate(sublines):
            if i < len(sublines) - 1:
                subl += '.'
            res, current_section = parse_article_line(subl, current_section, issue_theme)
            if res and res['title']:
                articles.append(res)

    return articles


def sanitize_bibtex_str(val):
    if not val:
        return ""
    val = str(val).strip()
    val = val.replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')
    return val


def format_bibtex_entry(item):
    cite_key = item['cite_key']
    fields = [
        f"  title = {{{sanitize_bibtex_str(item['title'])}}}",
        "  journal = {Pour la Science}"
    ]

    if item['authors']:
        fields.append(f"  author = {{{' and '.join(sanitize_bibtex_str(a) for a in item['authors'])}}}")

    if item['year']:
        fields.append(f"  year = {{{item['year']}}}")

    if item['month']:
        fields.append(f"  month = {{{item['month']:02d}}}")

    if item['issue_num'] is not None:
        fields.append(f"  number = {{{item['issue_num']}}}")

    fields.append(f"  url = {{{SOURCE_URL}}}")

    notes = []
    if item.get('issue_theme'):
        notes.append(f"Numéro spécial / Thème : {item['issue_theme']}")
    if item.get('section'):
        notes.append(f"Rubrique : {item['section']}")
    if item.get('raw_h2'):
        notes.append(f"Parution : {item['raw_h2']}")

    if notes:
        fields.append(f"  note = {{{sanitize_bibtex_str(' — '.join(notes))}}}")

    fields.append("  keywords = {Pour la Science; vulgarisation scientifique}")

    return f"@article{{{cite_key},\n" + ",\n".join(fields) + "\n}"


def format_ris_entry(item):
    lines = [
        "TY  - JOUR",
        f"TI  - {item['title']}",
        "JO  - Pour la Science"
    ]

    for auth in item['authors']:
        lines.append(f"AU  - {auth}")

    if item['year']:
        lines.append(f"PY  - {item['year']}")
        if item['month']:
            lines.append(f"DA  - {item['year']}/{item['month']:02d}//")
        else:
            lines.append(f"DA  - {item['year']}///")

    if item['issue_num'] is not None:
        lines.append(f"IS  - {item['issue_num']}")

    lines.append(f"UR  - {SOURCE_URL}")

    notes = []
    if item.get('issue_theme'):
        notes.append(f"Numéro spécial / Thème : {item['issue_theme']}")
    if item.get('section'):
        notes.append(f"Rubrique : {item['section']}")
    if item.get('raw_h2'):
        notes.append(f"Parution : {item['raw_h2']}")

    if notes:
        lines.append(f"N1  - {' — '.join(notes)}")

    lines.append("KW  - Pour la Science")
    lines.append("KW  - vulgarisation scientifique")
    lines.append("ER  - \n")

    return "\n".join(lines)


def main():
    raw_html = fetch_source_html()
    cleaned_html = fix_encoding_artifacts(raw_html)

    soup = BeautifulSoup(cleaned_html, 'html.parser')
    h2_list = soup.find_all('h2')
    tables = soup.find_all('table')

    print(f"Found {len(h2_list)} issues (H2) and {len(tables)} tables.")

    all_items = []

    for idx, (h2, t) in enumerate(zip(h2_list, tables)):
        issue_num, year, month, theme, raw_h2 = parse_h2(h2)
        articles = extract_articles_from_table(t, theme)

        for art_idx, art in enumerate(articles, start=1):
            first_author_slug = slugify(art['authors'][0].split()[-1]) if art['authors'] else slugify(art['title'][:20])
            num_str = str(issue_num) if issue_num is not None else f"idx{idx}"
            cite_key = f"pls_{num_str}_{art_idx}_{first_author_slug}"

            item = {
                'cite_key': cite_key,
                'issue_num': issue_num,
                'year': year,
                'month': month,
                'raw_h2': raw_h2,
                'issue_theme': theme,
                'title': art['title'],
                'authors': art['authors'],
                'section': art['section']
            }
            all_items.append(item)

    print(f"Extracted {len(all_items)} article references.")
    with_authors = sum(1 for it in all_items if it['authors'])
    print(f"  - With author(s): {with_authors}")
    print(f"  - Without author (briefs / editorials): {len(all_items) - with_authors}")

    # Generate BibTeX
    print("Writing BibTeX file...")
    bib_entries = [format_bibtex_entry(it) for it in all_items]
    with open(BIB_OUTPUT, 'w', encoding='utf-8') as f:
        f.write("% Bibliographic references from Pour la Science (1977-2014)\n")
        f.write(f"% Extracted from: {SOURCE_URL}\n")
        f.write(f"% Total entries: {len(bib_entries)}\n\n")
        f.write("\n\n".join(bib_entries) + "\n")

    # Generate RIS
    print("Writing RIS file...")
    ris_entries = [format_ris_entry(it) for it in all_items]
    with open(RIS_OUTPUT, 'w', encoding='utf-8') as f:
        f.write("\n".join(ris_entries) + "\n")

    print(f"\nSuccessfully generated:")
    print(f"  - {BIB_OUTPUT} ({len(bib_entries)} entries, {os.path.getsize(BIB_OUTPUT):,} bytes)")
    print(f"  - {RIS_OUTPUT} ({len(ris_entries)} entries, {os.path.getsize(RIS_OUTPUT):,} bytes)")


if __name__ == '__main__':
    main()
