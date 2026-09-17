#!/usr/bin/env python3
"""
Filter single-article tags before Hugo compilation.
Generates `content/tags/<slug>/_index.md` with:
---
build:
  render: never
  list: never
---
for all tags that appear in only 1 article.
Removes the marker file if a tag has more than 1 article.
"""

import os
import re
import unicodedata
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
TAGS_DIR = CONTENT_DIR / "tags"

TAG_RE = re.compile(r'^tags:\s*\n((?:\s*-\s*.*\n)+)', re.M)
DRAFT_RE = re.compile(r'^draft:\s*true\b', re.M | re.I)

def hugo_slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def main():
    tag_counts = Counter()
    
    # 1. Scan content files for tags
    for md_file in CONTENT_DIR.glob("**/*.md"):
        # Skip tags directory itself
        if TAGS_DIR in md_file.parents:
            continue
        try:
            with open(md_file, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
                if DRAFT_RE.search(content):
                    continue
                match = TAG_RE.search(content)
                if match:
                    for line in match.group(1).splitlines():
                        raw_tag = line.strip().lstrip("-").strip(" \"'")
                        if raw_tag:
                            slug = hugo_slugify(raw_tag)
                            if slug:
                                tag_counts[slug] += 1
        except Exception:
            pass

    print(f"Total distinct tag slugs: {len(tag_counts)}")
    single_tags = {slug for slug, count in tag_counts.items() if count <= 1}
    multi_tags = {slug for slug, count in tag_counts.items() if count > 1}
    print(f"Single-article tags to disable: {len(single_tags)}")
    print(f"Multi-article tags to render: {len(multi_tags)}")

    TAGS_DIR.mkdir(parents=True, exist_ok=True)
    
    marker_content = "---\nbuild:\n  render: never\n  list: never\n---\n"
    
    created = 0
    # 2. Write marker for single-article tags
    for slug in single_tags:
        term_dir = TAGS_DIR / slug
        term_file = term_dir / "_index.md"
        if not term_file.exists():
            term_dir.mkdir(parents=True, exist_ok=True)
            term_file.write_text(marker_content, encoding="utf-8")
            created += 1

    # 3. Remove markers for multi-article tags (in case count increased)
    removed = 0
    for slug in multi_tags:
        term_file = TAGS_DIR / slug / "_index.md"
        if term_file.exists():
            term_file.unlink()
            try:
                (TAGS_DIR / slug).rmdir()
            except OSError:
                pass
            removed += 1

    # 4. Clean any orphan empty dirs
    for item in TAGS_DIR.iterdir():
        if item.is_dir() and item.name not in single_tags:
            index = item / "_index.md"
            if index.exists():
                index.unlink()
            try:
                item.rmdir()
            except OSError:
                pass

    print(f"Done: {created} tag render-blockers created, {removed} removed.")

if __name__ == "__main__":
    main()
