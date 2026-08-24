#!/usr/bin/env python3
import os, glob, re, urllib.parse, shutil

site_dir = os.path.dirname(os.path.abspath(__file__))
posts_dir = os.path.join(site_dir, 'content/blog/posts')
uploads_dir = os.path.join(site_dir, 'static/wp-content/uploads')

all_md = sorted(glob.glob(os.path.join(posts_dir, '**/*.md'), recursive=True))

upload_index = {}
for root, dirs, files in os.walk(uploads_dir):
    for f in files:
        full_path = os.path.join(root, f)
        upload_index.setdefault(f.lower(), []).append(full_path)

def extract_image_refs(content):
    refs = []
    for m in re.finditer(r'!\[([^\]]*)\]\((.*?)\)', content):
        raw_target = m.group(2).strip()
        if raw_target.startswith('<') and '>' in raw_target:
            raw_target = raw_target[1:raw_target.index('>')]
        else:
            raw_target = re.split(r'\s+[\"\']', raw_target)[0].strip()
            raw_target = raw_target.split()[0] if raw_target.split() else ''
        if raw_target:
            refs.append(raw_target)
            
    for m in re.finditer(r'<img[^>]+src=[\"\']([^\"\'>]+)[\"\']', content, re.IGNORECASE):
        refs.append(m.group(1).strip())
        
    m = re.search(r'coverImage:\s*[\"\']?([^\"\'\n\r]+)[\"\']?', content)
    if m and m.group(1).strip():
        refs.append(m.group(1).strip())
        
    return list(dict.fromkeys(refs))

moved_count = 0
already_present_count = 0
missing_images = []

for md_path in all_md:
    year_dir = os.path.dirname(md_path)
    year_images_dir = os.path.join(year_dir, 'images')
    
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    filename = os.path.basename(md_path)
    date_m = re.search(r'date:\s*[\"\']?(\d{4}-\d{2}-\d{2})', content)
    title_m = re.search(r'title:\s*[\"\']?([^\"\'\n\r]+)[\"\']?', content)
    slug_m = re.search(r'slug:\s*[\"\']?([^\"\'\n\r]+)[\"\']?', content)
    
    post_title = title_m.group(1).strip() if title_m else filename
    
    if date_m:
        date_parts = date_m.group(1).split('-')
        year, month, day = date_parts[0], date_parts[1], date_parts[2]
    else:
        fn_match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-(.*)\.md$', filename)
        if fn_match:
            year, month, day = fn_match.group(1), fn_match.group(2), fn_match.group(3)
        else:
            year, month, day = '2020', '01', '01'
            
    if slug_m:
        slug = slug_m.group(1).strip()
    else:
        fn_match = re.match(r'^\d{4}-\d{2}-\d{2}-(.*)\.md$', filename)
        if fn_match:
            slug = fn_match.group(1)
        else:
            slug = filename.replace('.md', '')
            
    article_url = f'https://drgoulu.com/{year}/{month}/{day}/{slug}/'
    
    refs = extract_image_refs(content)
    for ref in refs:
        ref_clean = ref.split('?')[0].split('#')[0].strip()
        if not ref_clean or ref_clean.startswith('data:'):
            continue
            
        fname = os.path.basename(urllib.parse.unquote(ref_clean))
        if not fname:
            continue
            
        target_path = os.path.join(year_images_dir, fname)
        if os.path.exists(target_path):
            already_present_count += 1
        elif fname.lower() in upload_index:
            src_path = upload_index[fname.lower()][0]
            os.makedirs(year_images_dir, exist_ok=True)
            shutil.copy2(src_path, target_path)
            moved_count += 1
        else:
            if (ref_clean.startswith('http://') or ref_clean.startswith('https://')) and not ('drgoulu.com' in ref_clean or 'goulu.net' in ref_clean):
                continue
            missing_images.append({
                'article_url': article_url,
                'article_title': post_title,
                'post_file': os.path.relpath(md_path, site_dir),
                'image_name': fname,
                'raw_ref': ref
            })

html_out_path = os.path.join(site_dir, 'images_manquantes.html')
# HTML generation code ...
