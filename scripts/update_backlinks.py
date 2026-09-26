#!/usr/bin/env python3
"""
update_backlinks.py
Analyse tous les articles markdown dans content/ pour extraire les liens internes
et construire un index inversé (rétroliens / backlinks) sauvegardé dans data/backlinks.json.

Utilisé par layouts/_partials/page_related.html pour afficher en priorité dans
"Sur le même sujet" les articles citant l'article courant.
"""

import glob
import json
import os
import re
import sys
import time
from urllib.parse import urlparse, unquote

def extract_frontmatter(content):
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    return parts[1], parts[2]

def build_backlinks():
    t0 = time.time()
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    pattern_date = re.compile(r"^date:\s*['\"]?(\d{4}-\d{2}-\d{2})", re.MULTILINE)
    pattern_slug = re.compile(r"^slug:\s*['\"]?([^'\"\n\r]+)", re.MULTILINE)
    pattern_title = re.compile(r"^title:\s*['\"]?([^\n\r'\"]+)['\"]?", re.MULTILINE)
    pattern_draft = re.compile(r"^draft:\s*(true|false)", re.MULTILINE | re.IGNORECASE)
    pattern_aliases = re.compile(r"^aliases:\s*\n((?:\s*-\s*[^\n\r]+\n)+)", re.MULTILINE)
    pattern_link = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    date_filename_re = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")

    pages = {}          # canonical permalink -> {url, title, date}
    alias_to_perm = {}  # alias url -> canonical permalink
    file_to_perm = {}   # filepath -> (canonical permalink, markdown_body)

    md_files = glob.glob("content/**/*.md", recursive=True)

    # 1. Indexation de tous les articles et de leurs permaliens
    for fpath in md_files:
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
        except Exception:
            continue

        fm, body = extract_frontmatter(content)
        if not fm:
            continue

        dr_m = pattern_draft.search(fm)
        if dr_m and dr_m.group(1).lower() == "true":
            continue

        d_m = pattern_date.search(fm)
        fname = os.path.basename(fpath)
        year, month, day = None, None, None

        if d_m:
            raw_date = d_m.group(1).strip(" \"'")[:10]
            parts = raw_date.split("-")
            if len(parts) == 3:
                year, month, day = parts
        else:
            fn_m = date_filename_re.match(fname)
            if fn_m:
                year, month, day = fn_m.group(1), fn_m.group(2), fn_m.group(3)
                raw_date = f"{year}-{month}-{day}"

        if not (year and month and day):
            continue

        s_m = pattern_slug.search(fm)
        if s_m:
            slug = s_m.group(1).strip(" \"'")
        else:
            name_no_ext = os.path.splitext(fname)[0]
            slug = name_no_ext[11:] if date_filename_re.match(name_no_ext) else name_no_ext

        t_m = pattern_title.search(fm)
        title = t_m.group(1).strip() if t_m else slug

        permalink = f"/{year}/{month}/{day}/{slug}/"
        pages[permalink] = {
            "url": permalink,
            "title": title,
            "date": f"{year}-{month}-{day}"
        }
        file_to_perm[fpath] = (permalink, body)

        # Gestion des alias
        al_m = pattern_aliases.search(fm)
        if al_m:
            for line in al_m.group(1).splitlines():
                alias = line.strip("- \t\"'")
                if alias:
                    if not alias.startswith("/"): alias = "/" + alias
                    if not alias.endswith("/"): alias = alias + "/"
                    alias_to_perm[alias] = permalink
                    alias_to_perm[unquote(alias)] = permalink

    def resolve_target(dest):
        dest = dest.strip()
        parsed = urlparse(dest)
        if parsed.netloc and parsed.netloc not in ("drgoulu.com", "www.drgoulu.com"):
            return None
        path = parsed.path
        if not path or path == "/":
            return None
        if not path.startswith("/"):
            path = "/" + path
        if not path.endswith("/"):
            path = path + "/"

        path_unquote = unquote(path)

        if path in pages:
            return path
        if path_unquote in pages:
            return path_unquote
        if path in alias_to_perm:
            return alias_to_perm[path]
        if path_unquote in alias_to_perm:
            return alias_to_perm[path_unquote]
        return None

    # 2. Analyse des liens et construction des rétroliens
    backlinks = {}

    for fpath, (src_perm, body) in file_to_perm.items():
        src_page = pages[src_perm]
        seen_targets_in_article = set()

        for _, dest in pattern_link.findall(body):
            target = resolve_target(dest)
            if target and target != src_perm and target not in seen_targets_in_article:
                seen_targets_in_article.add(target)
                if target not in backlinks:
                    backlinks[target] = []
                backlinks[target].append({
                    "url": src_perm,
                    "title": src_page["title"],
                    "date": src_page["date"]
                })

    # 3. Tri chronologique décroissant (rétroliens les plus récents en premier)
    for target in backlinks:
        backlinks[target].sort(key=lambda x: x["date"], reverse=True)

    # 4. Écriture atomique dans data/backlinks.json si modifié
    os.makedirs("data", exist_ok=True)
    out_file = os.path.join(repo_root, "data", "backlinks.json")
    new_json = json.dumps(backlinks, ensure_ascii=False, indent=2)

    changed = True
    if os.path.exists(out_file):
        try:
            with open(out_file, "r", encoding="utf-8") as fp:
                if fp.read() == new_json:
                    changed = False
        except Exception:
            pass

    if changed:
        with open(out_file, "w", encoding="utf-8") as fp:
            fp.write(new_json)

    elapsed = time.time() - t0
    total_links = sum(len(v) for v in backlinks.values())
    status_str = "mis à jour" if changed else "inchangé (à jour)"
    print(f"✅ Index des rétroliens {status_str} en {elapsed:.2f}s : {len(backlinks)} cibles avec rétroliens ({total_links} liens totaux).")

if __name__ == "__main__":
    build_backlinks()
