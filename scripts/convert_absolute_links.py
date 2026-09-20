#!/usr/bin/env python3
import os
import re
import urllib.parse

def build_valid_urls():
    valid_urls = set()
    date_re = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")

    # 1. Inspect all markdown content frontmatter
    for root, dirs, files in os.walk("content"):
        for f in files:
            if not f.endswith(".md"):
                continue
            filepath = os.path.join(root, f)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
            except Exception:
                continue

            if not content.startswith("---"):
                continue
            parts = content.split("---", 2)
            if len(parts) < 3:
                continue
            frontmatter = parts[1]

            date_m = re.search(r"^date:\s*['\"]?(\d{4}-\d{2}-\d{2})", frontmatter, re.MULTILINE)
            slug_m = re.search(r"^slug:\s*['\"]?([^'\"\n\r]+)", frontmatter, re.MULTILINE)

            year, month, day = None, None, None
            if date_m:
                year, month, day = date_m.group(1).split("-")
            else:
                fn_m = date_re.match(f)
                if fn_m:
                    year, month, day = fn_m.group(1), fn_m.group(2), fn_m.group(3)

            slug = None
            if slug_m:
                slug = slug_m.group(1).strip()
            else:
                name = f[:-3]
                slug = name[11:] if date_re.match(name) else name

            if year and month and day and slug:
                perm = f"/{year}/{month}/{day}/{slug}/"
                valid_urls.add(perm)
                valid_urls.add(perm.rstrip("/"))
                valid_urls.add(urllib.parse.unquote(perm))
                valid_urls.add(urllib.parse.unquote(perm.rstrip("/")))

            if "aliases:" in frontmatter:
                alias_section = frontmatter[frontmatter.find("aliases:"):]
                next_key = re.search(r"^[a-zA-Z0-9_-]+:", alias_section[8:], re.MULTILINE)
                if next_key:
                    alias_section = alias_section[:8 + next_key.start()]
                alias_lines = re.findall(r"^\s*-\s*['\"]?([^'\"\n\r]+)", alias_section, re.MULTILINE)
                for a in alias_lines:
                    a_clean = a.strip()
                    if not a_clean.startswith("/"):
                        a_clean = "/" + a_clean
                    valid_urls.add(a_clean)
                    valid_urls.add(a_clean.rstrip("/") + "/")
                    valid_urls.add(urllib.parse.unquote(a_clean))
                    valid_urls.add(urllib.parse.unquote(a_clean.rstrip("/") + "/"))

    # 2. Inspect public directory
    if os.path.exists("public"):
        for root, dirs, files in os.walk("public"):
            if "index.html" in files:
                rel = os.path.relpath(root, "public")
                if rel != ".":
                    valid_urls.add("/" + rel + "/")
                    valid_urls.add("/" + rel)
                    valid_urls.add(urllib.parse.unquote("/" + rel + "/"))
                    valid_urls.add(urllib.parse.unquote("/" + rel))

    # 3. Inspect public/_redirects
    if os.path.exists("public/_redirects"):
        with open("public/_redirects", "r", encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) >= 2:
                        valid_urls.add(parts[0])
                        valid_urls.add(parts[0].rstrip("/") + "/")
                        valid_urls.add(urllib.parse.unquote(parts[0]))

    return valid_urls

def main():
    print("Construction de l'index des destinations valides...")
    valid_urls = build_valid_urls()
    print(f"Index prêt ({len(valid_urls)} chemins valides répertoriés).")

    # Regex pour capturer les liens absolus vers drgoulu.com au format AAAA/MM/JJ/slug
    pattern = re.compile(r"\]\((https?://(?:www\.)?drgoulu\.com/(\d{4}/\d{2}/\d{2}/[^/)\"\s\x27\<\>#]+)/?(#[^)\"\s\x27\<\>]*)?)\)")

    total_links_scanned = 0
    converted_count = 0
    errors_list = []
    files_modified_count = 0
    total_files_scanned = 0

    for root, dirs, files in os.walk("content"):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            total_files_scanned += 1
            filepath = os.path.join(root, f)

            with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
                lines = fp.readlines()

            file_modified = False
            new_lines = []

            for line_no, line in enumerate(lines, 1):
                matches = list(pattern.finditer(line))
                if not matches:
                    new_lines.append(line)
                    continue

                new_line = line
                # Remplacement de droite à gauche pour préserver les indices
                for m in reversed(matches):
                    total_links_scanned += 1
                    full_url = m.group(1)
                    slug_path = "/" + m.group(2) + "/"
                    frag = m.group(3) or ""
                    unquoted = urllib.parse.unquote(slug_path)

                    # Vérification de l'existence de la destination
                    is_valid = (
                        slug_path in valid_urls or
                        slug_path.rstrip("/") in valid_urls or
                        unquoted in valid_urls or
                        unquoted.rstrip("/") in valid_urls
                    )

                    if is_valid:
                        file_modified = True
                        converted_count += 1
                        replacement = f"]({slug_path}{frag})"
                        new_line = new_line[:m.start()] + replacement + new_line[m.end():]
                    else:
                        errors_list.append((filepath, line_no, full_url, slug_path))

                new_lines.append(new_line)

            if file_modified:
                with open(filepath, "w", encoding="utf-8") as fp:
                    fp.writelines(new_lines)
                files_modified_count += 1

    # Écriture du fichier errors.log
    errors_log_path = "errors.log"
    with open(errors_log_path, "w", encoding="utf-8") as fp:
        fp.write(f"# Journal des erreurs de conversion de liens absolus drgoulu.com\n")
        fp.write(f"# Total liens non trouvés : {len(errors_list)}\n\n")
        for filepath, line_no, full_url, slug_path in errors_list:
            fp.write(f"{filepath}:{line_no}: {full_url} (destination {slug_path} introuvable)\n")

    print("\n=== Résultat du traitement ===")
    print(f"Fichiers Markdown scannés : {total_files_scanned}")
    print(f"Fichiers modifiés         : {files_modified_count}")
    print(f"Liens absolus détectés    : {total_links_scanned}")
    print(f"Liens convertis en relatifs: {converted_count}")
    print(f"Liens inexistants (logués): {len(errors_list)}")
    print(f"Journal généré dans       : {errors_log_path}")

if __name__ == "__main__":
    main()
