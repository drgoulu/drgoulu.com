#!/usr/bin/env python3
"""
scripts/rename_posts_by_slug.py
Renomme tous les fichiers .md dans content/posts/ selon leur champ 'slug'.
Si un slug a été tronqué à la virgule (ex: 'pourquoi' ou 'bonjour' pour une question Quora complète),
le slug est recalculé à partir du titre sans considérer la virgule comme délimiteur,
et mis à jour dans le front-matter du fichier.
Pour les fichiers ayant le même slug dans le même dossier d'année (collisions) :
- fusionne le contenu et les métadonnées dans un fichier unique <slug>.md
- si les fichiers ont la même date et le même contenu, conserve le nom de fichier le plus long,
  supprime le plus court et ne l'inscrit pas dans collisions.txt
- consigne la liste détaillée des vraies fusions (dates ou contenus différents) dans 'collisions.txt'.
"""

import os
import re
import sys
import yaml
from unicodedata import normalize

POSTS_DIR = "content/posts"
COLLISIONS_FILE = "collisions.txt"

def slugify(text, max_length=235):
    """Normalise les accents et génère un slug propre pour Hugo."""
    text = normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    if max_length and len(slug) > max_length:
        slug = slug[:max_length]
        if "-" in slug:
            slug = slug.rsplit("-", 1)[0]
    return slug

def compute_clean_slug(title, existing_slug, max_length=235):
    """
    Corrige les slugs qui ont été tronqués à la virgule ou sur un mot d'introduction
    (ex: 'pourquoi' ou 'bonjour') alors que le titre est une question Quora complète.
    """
    if "," in title:
        before_comma = slugify(title.split(",")[0], max_length=None)
        if existing_slug == before_comma:
            full = slugify(title, max_length=max_length)
            if full != existing_slug:
                return full
    if existing_slug in ["bonjour", "bonjours", "pourquoi", "comment", "combien", "qui", "quoi"] and len(title.split()) > 3:
        return slugify(title, max_length=max_length)
    return existing_slug

def parse_markdown(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    if text.startswith("---"):
        parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return fm, body, text, parts
            except Exception as e:
                print(f"Warning parsing YAML in {filepath}: {e}", file=sys.stderr)
    return {}, text.strip(), text, []

def merge_collision_group(file_paths, target_path, target_slug):
    parsed = [parse_markdown(p) for p in file_paths]

    # 1. Title: prefer non-draft, or first available
    titles = [fm.get("title") for fm, _, _, _ in parsed if fm.get("title")]
    best_title = titles[0] if titles else ""
    for fm, _, _, _ in parsed:
        if not fm.get("draft", False) and fm.get("title"):
            best_title = fm["title"]
            break

    # 2. Date: earliest date
    dates = [str(fm.get("date")) for fm, _, _, _ in parsed if fm.get("date")]
    dates.sort()
    best_date = dates[0] if dates else ""

    # 3. Draft: false if any is false
    is_draft = all(fm.get("draft", False) for fm, _, _, _ in parsed)

    # 4. Slug: target_slug
    slug = target_slug

    # 5. Tags union preserving order
    merged_tags = []
    for fm, _, _, _ in parsed:
        for t in fm.get("tags") or []:
            if t and t not in merged_tags:
                merged_tags.append(t)

    # 6. Categories union preserving order
    merged_categories = []
    for fm, _, _, _ in parsed:
        for c in fm.get("categories") or []:
            if c and c not in merged_categories:
                merged_categories.append(c)

    # 7. CoverImage: first available
    cover_image = ""
    for fm, _, _, _ in parsed:
        if fm.get("coverImage"):
            cover_image = fm["coverImage"]
            break

    merged_fm = {
        "title": best_title,
        "date": best_date,
        "draft": is_draft,
        "tags": merged_tags,
        "categories": merged_categories,
        "slug": slug,
    }
    if cover_image:
        merged_fm["coverImage"] = cover_image

    # 8. Body merging
    bodies = []
    for (fm, body, _, _), p in zip(parsed, file_paths):
        b = body.strip()
        if not b:
            continue
        # Avoid exact duplicate content
        if any(b == existing or (len(b) > 50 and b in existing) for existing in bodies):
            continue
        # If this body contains a shorter existing body, replace it
        replace_idx = None
        for idx, existing in enumerate(bodies):
            if len(existing) > 50 and existing in b:
                replace_idx = idx
                break
        if replace_idx is not None:
            bodies[replace_idx] = b
        else:
            bodies.append(b)

    merged_body = "\n\n---\n\n".join(bodies)
    yaml_str = yaml.dump(merged_fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    return f"---\n{yaml_str}---\n\n{merged_body}\n"

def main():
    dry_run = "--dry-run" in sys.argv
    groups = {}  # (root, target_fname) -> [source_filenames]
    slug_corrections = {}  # filepath -> new_slug

    print(f"Scanning {POSTS_DIR}...")
    for root, dirs, files in os.walk(POSTS_DIR):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            fm, _, _, _ = parse_markdown(path)
            raw_slug = str(fm.get("slug") or "")
            title = str(fm.get("title") or "")
            
            clean_slug = compute_clean_slug(title, raw_slug)
            if not clean_slug:
                clean_slug = slugify(title, max_length=235)
                
            if clean_slug != raw_slug:
                slug_corrections[path] = clean_slug

            target_fname = f"{clean_slug}.md"
            key = (root, target_fname)
            groups.setdefault(key, []).append(f)

    total_files = sum(len(flist) for flist in groups.values())
    collision_groups = {k: v for k, v in groups.items() if len(v) > 1}
    single_groups = {k: v[0] for k, v in groups.items() if len(v) == 1}

    print(f"Found {total_files} .md files.")
    print(f"Slugs to update (comma/greeting delimiter fix): {len(slug_corrections)}")
    print(f"Direct renames (no collision): {len(single_groups)}")
    print(f"Collision groups to merge: {len(collision_groups)} ({sum(len(v) for v in collision_groups.values())} files)")

    if dry_run:
        print("Dry run requested, exiting without modifications.")
        return

    # 1. Mise à jour des slugs dans le front-matter des fichiers concernés
    print("Updating front-matter slugs...")
    for path, new_slug in slug_corrections.items():
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            text = fp.read()
        parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            new_fm_str = re.sub(r"^slug:.*$", f"slug: {new_slug}", parts[1], flags=re.MULTILINE)
            new_text = f"---\n{new_fm_str}---\n{parts[2]}"
            with open(path, "w", encoding="utf-8") as out:
                out.write(new_text)

    # 2. Traitement des collisions
    print("Processing collisions...")
    collision_logs = []
    identical_duplicates_count = 0
    for (root, target_fname), flist in sorted(collision_groups.items(), key=lambda x: (x[0][0], x[0][1])):
        flist.sort()
        file_paths = [os.path.join(root, f) for f in flist]
        target_path = os.path.join(root, target_fname)
        target_slug = os.path.splitext(target_fname)[0]

        parsed = [parse_markdown(p) for p in file_paths]
        dates = set(str(fm.get("date", "")) for fm, _, _, _ in parsed)
        bodies = [body.strip() for _, body, _, _ in parsed]
        same_date = len(dates) == 1
        same_body = all(b == bodies[0] for b in bodies)

        merged_content = merge_collision_group(file_paths, target_path, target_slug)

        # Write merged target
        with open(target_path, "w", encoding="utf-8") as out:
            out.write(merged_content)

        # Delete original files that are not target_path
        for p in file_paths:
            if p != target_path:
                os.remove(p)

        # Si même date et même contenu, il s'agissait d'un simple doublon avec nom tronqué
        # On ne consigne dans collisions.txt que les vraies fusions nécessitant un suivi
        if same_date and same_body:
            identical_duplicates_count += 1
        else:
            collision_logs.append({
                "target": target_path,
                "sources": file_paths,
            })

    # 3. Traitement des renommages simples
    print("Processing single renames...")
    renamed_count = 0
    for (root, target_fname), orig_fname in single_groups.items():
        src = os.path.join(root, orig_fname)
        dst = os.path.join(root, target_fname)
        if src != dst:
            os.rename(src, dst)
            renamed_count += 1

    # 4. Écriture du rapport collisions.txt
    with open(COLLISIONS_FILE, "w", encoding="utf-8") as out:
        out.write(f"Rapport des collisions résolues par fusion ({len(collision_logs)} fusions)\n")
        out.write(f"Date d'exécution : 2026-09-27\n")
        out.write("=" * 80 + "\n\n")
        for entry in collision_logs:
            out.write(f"Fichier cible : {entry['target']}\n")
            out.write(f"Articles d'origine fusionnés ({len(entry['sources'])}) :\n")
            for src in entry["sources"]:
                out.write(f"  - {os.path.basename(src)}\n")
            out.write("\n" + "-" * 80 + "\n\n")

    print(f"Terminé avec succès !")
    print(f"- {len(slug_corrections)} slugs mis à jour dans le front-matter.")
    print(f"- {renamed_count} fichiers renommés.")
    print(f"- {identical_duplicates_count} doublons identiques éliminés (même date & contenu, nom plus court supprimé).")
    print(f"- {len(collision_logs)} groupes de vraies collisions fusionnés et consignés dans {COLLISIONS_FILE}.")

if __name__ == "__main__":
    main()
