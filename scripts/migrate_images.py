#!/usr/bin/env python3
"""
Migrate and normalize all images referenced by articles to content/posts/YYYY/images/
with relative path ./images/<filename>.
"""

import os
import sys
import glob
import re
import urllib.parse
import shutil
import argparse

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp', '.ico'}

def is_image_file(name, year_images_dir=None):
    _, ext = os.path.splitext(name.lower())
    if ext in IMAGE_EXTENSIONS:
        return True
    if year_images_dir and os.path.exists(os.path.join(year_images_dir, name)):
        return True
    return False

def clean_ref_target(raw_target):
    target = raw_target.strip()
    if target.startswith('<') and '>' in target:
        target = target[1:target.index('>')]
    else:
        target = re.split(r'\s+[\"\']', target)[0].strip()
        target = target.split()[0] if target.split() else ''
    return target

def build_indices(site_dir):
    static_dir = os.path.join(site_dir, 'static')
    posts_dir = os.path.join(site_dir, 'content/posts')

    static_index = {}
    for root, dirs, files in os.walk(static_dir):
        for f in files:
            full_path = os.path.join(root, f)
            static_index.setdefault(f.lower(), []).append(full_path)

    post_images_index = {}
    for root, dirs, files in os.walk(posts_dir):
        if os.path.basename(root) == 'images':
            for f in files:
                full_path = os.path.join(root, f)
                post_images_index.setdefault(f.lower(), []).append(full_path)

    return static_index, post_images_index

def find_source_image(fname, year, static_index, post_images_index):
    fname_lower = fname.lower()
    # Check post_images_index first
    if fname_lower in post_images_index:
        # Prefer exact match in another year
        return post_images_index[fname_lower][0]
    # Check static_index
    if fname_lower in static_index:
        return static_index[fname_lower][0]
    return None

def main():
    parser = argparse.ArgumentParser(description="Migrate images to content/posts/YYYY/images/")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without writing files")
    parser.add_argument('--cleanup-static', action='store_true', help="Remove duplicate images from static/")
    args = parser.parse_args()

    site_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(site_dir, 'content/posts')
    all_md = sorted(glob.glob(os.path.join(posts_dir, '**/*.md'), recursive=True))

    static_index, post_images_index = build_indices(site_dir)

    stats = {
        'total_posts': len(all_md),
        'posts_modified': 0,
        'images_copied': 0,
        'cover_updated': 0,
        'md_img_updated': 0,
        'html_img_updated': 0,
        'figure_updated': 0,
        'links_updated': 0,
        'missing_images': [],
    }

    copied_destinations = set()

    for md_path in all_md:
        rel_path = os.path.relpath(md_path, site_dir)
        parts = rel_path.split(os.sep)
        # rel_path is content/posts/YYYY/filename.md
        if len(parts) < 4 or parts[0] != 'content' or parts[1] != 'posts':
            continue
        year = parts[2]
        year_images_dir = os.path.join(site_dir, 'content', 'posts', year, 'images')

        with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
            original_content = f.read()

        modified_content = original_content

        def ensure_image_exists(fname):
            nonlocal static_index, post_images_index
            target_path = os.path.join(year_images_dir, fname)
            if os.path.exists(target_path) or target_path in copied_destinations:
                return True

            src_path = find_source_image(fname, year, static_index, post_images_index)
            if src_path and os.path.exists(src_path):
                stats['images_copied'] += 1
                copied_destinations.add(target_path)
                if not args.dry_run:
                    os.makedirs(year_images_dir, exist_ok=True)
                    shutil.copy2(src_path, target_path)
                    # Update index
                    post_images_index.setdefault(fname.lower(), []).append(target_path)
                return True
            else:
                stats['missing_images'].append((rel_path, fname))
                return False

        # 1. Update coverImage in frontmatter
        def replace_cover(match):
            nonlocal modified_content
            raw_val = match.group(1).strip()
            # If already ./images/<filename>, keep
            if raw_val.startswith('./images/'):
                fname = raw_val[len('./images/'):]
                ensure_image_exists(fname)
                return match.group(0)

            clean = urllib.parse.unquote(raw_val.split('?')[0].split('#')[0])
            fname = os.path.basename(clean)
            if is_image_file(fname, year_images_dir):
                ensure_image_exists(fname)
                stats['cover_updated'] += 1
                return f'coverImage: "./images/{fname}"'
            return match.group(0)

        modified_content = re.sub(r'^coverImage:\s*[\"\']?([^\"\'\r\n]+)[\"\']?', replace_cover, modified_content, flags=re.MULTILINE)

        # 2. Update Hugo figure shortcodes: {{< figure src="..." ... >}}
        def replace_figure(match):
            full_shortcode = match.group(0)
            src_match = re.search(r'src="([^"]+)"', full_shortcode) or re.search(r"src='([^']+)'", full_shortcode)
            if not src_match:
                return full_shortcode

            raw_src = src_match.group(1).strip()
            if raw_src.startswith('http://') or raw_src.startswith('https://'):
                # External url, check if it's pointing to drgoulu wp-content
                if not ('drgoulu.com/wp-content/uploads' in raw_src or 'goulu.wordpress.com/wp-content/uploads' in raw_src):
                    return full_shortcode

            clean = urllib.parse.unquote(raw_src.split('?')[0].split('#')[0])
            fname = os.path.basename(clean)

            ensure_image_exists(fname)
            new_shortcode = full_shortcode.replace(f'src="{raw_src}"', f'src="./images/{fname}"')
            new_shortcode = new_shortcode.replace(f"src='{raw_src}'", f'src="./images/{fname}"')

            # Also check if link in figure points to /wp-content/uploads/.../<fname> or images/<fname>
            link_match = re.search(r'link="([^"]+)"', new_shortcode) or re.search(r"link='([^']+)'", new_shortcode)
            if link_match:
                raw_link = link_match.group(1).strip()
                link_fname = os.path.basename(urllib.parse.unquote(raw_link.split('?')[0].split('#')[0]))
                if is_image_file(link_fname, year_images_dir) and ('wp-content/uploads' in raw_link or raw_link.startswith('images/') or raw_link.startswith('/images/')):
                    ensure_image_exists(link_fname)
                    new_shortcode = new_shortcode.replace(f'link="{raw_link}"', f'link="./images/{link_fname}"')
                    new_shortcode = new_shortcode.replace(f"link='{raw_link}'", f'link="./images/{link_fname}"')
                    stats['links_updated'] += 1

            if new_shortcode != full_shortcode:
                stats['figure_updated'] += 1
            return new_shortcode

        modified_content = re.sub(r'\{\{<\s*figure\b[^>]*>\}\}', replace_figure, modified_content)

        # 3. Update Markdown images: ![alt](target)
        def replace_md_img(match):
            alt_text = match.group(1)
            raw_target = match.group(2)
            clean_target = clean_ref_target(raw_target)

            if not clean_target:
                return match.group(0)

            if clean_target.startswith('http://') or clean_target.startswith('https://'):
                if not ('drgoulu.com/wp-content/uploads' in clean_target or 'goulu.wordpress.com/wp-content/uploads' in clean_target):
                    return match.group(0)

            clean = urllib.parse.unquote(clean_target.split('?')[0].split('#')[0])
            fname = os.path.basename(clean)
            if not is_image_file(fname, year_images_dir):
                return match.group(0)

            ensure_image_exists(fname)
            new_target = raw_target.replace(clean_target, f'./images/{fname}')
            stats['md_img_updated'] += 1
            return f'![{alt_text}]({new_target})'

        modified_content = re.sub(r'!\[([^\]]*)\]\((.*?)\)', replace_md_img, modified_content)

        # 4. Update HTML img tags: <img ... src="..." ...>
        def replace_html_img(match):
            tag = match.group(0)
            src_val = match.group(1)
            if src_val.startswith('http://') or src_val.startswith('https://'):
                if not ('drgoulu.com/wp-content/uploads' in src_val or 'goulu.wordpress.com/wp-content/uploads' in src_val):
                    return tag

            clean = urllib.parse.unquote(src_val.split('?')[0].split('#')[0])
            fname = os.path.basename(clean)
            if not is_image_file(fname, year_images_dir):
                return tag

            ensure_image_exists(fname)
            stats['html_img_updated'] += 1
            return tag.replace(f'src="{src_val}"', f'src="./images/{fname}"').replace(f"src='{src_val}'", f'src="./images/{fname}"')

        modified_content = re.sub(r'<img[^>]+src=[\"\']([^\"\'>]+)[\"\'][^>]*>', replace_html_img, modified_content, flags=re.IGNORECASE)

        # 5. Update image wrapping links pointing to /wp-content/uploads/... or images/...
        # e.g. [![](...)](/wp-content/uploads/... "title") or [![](...)](images/... "title")
        def replace_img_links(match):
            raw_target = match.group(1)
            clean_target = clean_ref_target(raw_target)
            clean = urllib.parse.unquote(clean_target.split('?')[0].split('#')[0])
            fname = os.path.basename(clean)

            if is_image_file(fname, year_images_dir) and ('wp-content/uploads' in clean_target or clean_target.startswith('/uploads/') or clean_target.startswith('images/') or clean_target.startswith('/images/')):
                ensure_image_exists(fname)
                stats['links_updated'] += 1
                new_target = raw_target.replace(clean_target, f'./images/{fname}')
                return f']({new_target})'
            return match.group(0)

        modified_content = re.sub(r'\]\((/(?:wp-content/uploads|uploads)/[^\)]+|/?images/[^\)]+)\)', replace_img_links, modified_content)

        if modified_content != original_content:
            stats['posts_modified'] += 1
            if not args.dry_run:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)

    print("=" * 60)
    print(f"MIGRATION REPORT ({'DRY-RUN' if args.dry_run else 'EXECUTED'})")
    print("=" * 60)
    print(f"Total posts checked:       {stats['total_posts']}")
    print(f"Posts modified:            {stats['posts_modified']}")
    print(f"Images copied to /images/: {stats['images_copied']}")
    print(f"coverImage updated:        {stats['cover_updated']}")
    print(f"Markdown ![]() updated:    {stats['md_img_updated']}")
    print(f"HTML <img> updated:        {stats['html_img_updated']}")
    print(f"Figure shortcodes updated: {stats['figure_updated']}")
    print(f"Links to images updated:   {stats['links_updated']}")
    print(f"Missing images not found:  {len(stats['missing_images'])}")
    if stats['missing_images']:
        print("\nMissing images (first 10):")
        for post, img in stats['missing_images'][:10]:
            print(f"  - {post}: {img}")
    print("=" * 60)

    if args.cleanup_static and not args.dry_run:
        print("\nCleaning up redundant images in static/...")
        # Reload post images index
        _, post_images_index = build_indices(site_dir)
        deleted_count = 0
        static_dirs_to_clean = [
            os.path.join(site_dir, 'static', 'wp-content', 'uploads'),
            os.path.join(site_dir, 'static', 'uploads'),
        ]
        for sdir in static_dirs_to_clean:
            if not os.path.exists(sdir):
                continue
            for root, dirs, files in os.walk(sdir, topdown=False):
                for f in files:
                    if is_image_file(f) and f.lower() in post_images_index:
                        fpath = os.path.join(root, f)
                        os.remove(fpath)
                        deleted_count += 1
                if root != sdir and not os.listdir(root):
                    os.rmdir(root)
        print(f"Removed {deleted_count} duplicate image files from static directories.")

if __name__ == '__main__':
    main()
