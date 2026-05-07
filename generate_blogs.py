import os
import re
import yaml
from datetime import datetime
from pathlib import Path

try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    markdown = None

def find_md_files_in_blog_folders():
    """Find all .md files in blog subfolders"""
    blog_dir = Path('blog')
    md_files = []
    
    if not blog_dir.exists():
        print("Blog directory not found!")
        return md_files
    
    for folder in blog_dir.iterdir():
        if folder.is_dir() and folder.name != '__pycache__':
            # Look for .md files in this folder
            for file in folder.iterdir():
                if file.suffix == '.md':
                    md_files.append(file)
    
    return md_files

def extract_metadata_from_md(md_file_path):
    """Extract Date, Overview, Private, and Title from markdown file, supporting both
    YAML frontmatter (--- delimited) and legacy inline format. Returns cleaned content."""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    date = None
    overview = None
    is_private = False
    title = None

    # Try YAML frontmatter first
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if yaml_match:
        try:
            frontmatter = yaml.safe_load(yaml_match.group(1))
            if frontmatter:
                date = str(frontmatter.get('date', date)) if frontmatter.get('date') else date
                overview = frontmatter.get('overview', overview) or frontmatter.get('description', overview)
                is_private = frontmatter.get('private', is_private) or frontmatter.get('draft', is_private)
                title = frontmatter.get('title', title)
            content = content[yaml_match.end():]
        except yaml.YAMLError:
            pass

    # Fall back to legacy inline format
    if not date:
        date_match = re.search(r'^Date:\s*(.+)$', content, re.MULTILINE)
        date = date_match.group(1).strip() if date_match else "Unknown Date"
    if not overview:
        overview_match = re.search(r'^Overview:\s*(.+)$', content, re.MULTILINE)
        overview = overview_match.group(1).strip() if overview_match else "No description available"
    if not is_private:
        private_match = re.search(r'^Private:\s*(.+)$', content, re.MULTILINE)
        is_private = private_match.group(1).strip().lower() == 'true' if private_match else False

    # Remove legacy Date, Overview, Private lines (already removed from frontmatter)
    content = re.sub(r'^Date:\s*.+$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Overview:\s*.+$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Private:\s*.+$', '', content, flags=re.MULTILINE)

    # Clean up extra newlines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    return date, overview, is_private, content.strip(), title

def convert_md_to_html(md_content, title):
    """Convert markdown content to HTML"""
    if not HAS_MARKDOWN:
        return f"<pre>{md_content}</pre>"
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'admonition', 'sane_lists'])
    return html_content

def create_html_from_template(title, html_content, folder_name, is_private=False):
    """Create HTML file using template"""
    # Read template
    with open('blog/template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholders
    html_output = template.replace('Add your title here', title)
    
    # Create password protection if private
    if is_private:
        blog_structure = f'''<div class="content">
            <div id="password-prompt" class="password-container">
                <h2>This is a private post</h2>
                <p>Please enter the password to view this content:</p>
                <input type="password" id="password-input" placeholder="Enter password">
                <button onclick="checkPassword()">Submit</button>
                <div id="error-message" style="color: red; margin-top: 10px; display: none;">Incorrect password. Please try again.</div>
            </div>
            <div id="protected-content" style="display: none;">
                <article class="page sans">
                    <header>
                        <h1 class="page-title">{title}</h1>
                        <p class="page-description"></p>
                    </header>
                    <div class="page-body">
{html_content}
                    </div>
                </article>
            </div>
        </div>
        <script>
            function checkPassword() {{
                const password = document.getElementById('password-input').value;
                const correctPassword = 'alvaro';
                
                if (password === correctPassword) {{
                    document.getElementById('password-prompt').style.display = 'none';
                    document.getElementById('protected-content').style.display = 'block';
                }} else {{
                    document.getElementById('error-message').style.display = 'block';
                    document.getElementById('password-input').value = '';
                }}
            }}
            
            // Allow Enter key to submit password
            document.getElementById('password-input').addEventListener('keypress', function(e) {{
                if (e.key === 'Enter') {{
                    checkPassword();
                }}
            }});
        </script>'''
    else:
        # Create the proper blog structure matching existing blogs
        blog_structure = f'''<div class="content">
            <article class="page sans">
                <header>
                    <h1 class="page-title">{title}</h1>
                    <p class="page-description"></p>
                </header>
                <div class="page-body">
{html_content}
                </div>
            </article>
        </div>'''
    
    html_output = html_output.replace('your_iframe_here', blog_structure)
    
    # Add the proper styling that matches existing blogs
    new_style = '''
        .page-title {
            margin-top: 0;
            font-size: 2.5rem;
            margin-bottom: -1.0rem;
        }
        .page-description {
            color: #666;
            margin-bottom: 1.5rem;
        }
        .page-body {
            line-height: 1.6;
            margin-top: 2rem;
        }
        .page-body ul {
            list-style-type: disc;
            padding-left: 2rem;
            margin-bottom: 1.5rem;
        }
        .page-body ol {
            list-style-type: decimal;
            padding-left: 2rem;
            margin-bottom: 1.5rem;
        }
        .page-body li {
            margin-bottom: 0.5rem;
        }
        .page-body li p {
            margin-bottom: 0;
        }
        .image {
            margin: 1.5rem 0;
            text-align: center;
        }
        .image img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* Admonition styles */
        .admonition {
            border-left: 4px solid var(--accent-color, #007bff);
            padding: 1rem 1.5rem;
            margin: 2rem 0;
            background: rgba(0, 123, 255, 0.05);
            border-radius: 0 8px 8px 0;
        }
        .admonition-title {
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--accent-color, #007bff);
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
        }
        .admonition p:last-child {
            margin-bottom: 0;
        }
        
        /* Password protection styles */
        .password-container {
            text-align: center;
            padding: 2rem;
            max-width: 400px;
            margin: 0 auto;
            background-color: var(--bg-color);
            color: var(--text-color);
        }
        
        .password-container h2 {
            margin-bottom: 1rem;
            color: var(--text-color);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 600;
        }
        
        .password-container p {
            margin-bottom: 1.5rem;
            color: var(--text-color);
            opacity: 0.8;
        }
        
        .password-container input {
            padding: 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            width: 200px;
            margin-right: 0.5rem;
            font-size: 1rem;
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .password-container input:focus {
            outline: none;
            border-color: var(--accent-color);
        }
        
        .password-container button {
            padding: 0.75rem 1.5rem;
            background-color: var(--accent-color);
            color: var(--bg-color);
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 500;
        }
        
        .password-container button:hover {
            opacity: 0.9;
        }
        
        .error-message {
            color: #e74c3c;
            margin-top: 1rem;
            font-size: 0.9rem;
        }
        
        /* Override the existing carousel styles to show all images in a grid */
        .image-carousel {
            display: grid !important;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)) !important;
            gap: 1rem !important;
            margin: 2rem 0 !important;
            position: static !important;
            overflow: visible !important;
        }
        
        .carousel-item {
            display: block !important;
            text-align: center !important;
        }
        
        .carousel-item img {
            width: 100% !important;
            border-radius: 8px !important;
            max-width: 100% !important;
            height: auto !important;
        }
        
        .carousel-description {
            margin-top: 0.5rem !important;
            font-size: 0.9rem !important;
            color: #666 !important;
            font-style: normal !important;
        }
    '''
    
    html_output = html_output.replace(
        '<style>\n        .page-container {\n            display: flex;\n            justify-content: center;\n            /* horizontal */\n            align-items: center;\n            /* vertical */\n            height: 100vh;\n            /* full viewport height */\n        }\n\n        iframe {\n            width: 500px;\n            height: 600px;\n            border: none;\n        }\n    </style>',
        f'<style>{new_style}</style>'
    )
    
    # Also fix the placeholder container to avoid double nesting
    html_output = html_output.replace(
        '<div class="page-container">\n        your_iframe_here\n    </div>',
        'your_iframe_here'
    )
    
    return html_output


# ─── Blog listing helpers ───────────────────────────────────────────────

def extract_title_from_html(html_content):
    """Extract blog title from an index.html file."""
    # Try <h1> first (most specific)
    h1_match = re.search(r'<h1[^>]*>\s*(.+?)\s*</h1>', html_content, re.DOTALL)
    if h1_match:
        return h1_match.group(1).strip()
    # Fall back to <title> tag
    title_match = re.search(r'<title>\s*(.+?)\s*</title>', html_content, re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        title = re.sub(r'\s*-\s*Álvaro Menéndez.*$', '', title).strip()
        return title
    return "Untitled"


def extract_date_from_html(html_content):
    """Extract date from HTML meta or content."""
    date_match = re.search(r'<meta name="date" content="([^"]+)"', html_content)
    if date_match:
        return date_match.group(1).strip()
    pm_match = re.search(r'class="post-meta"[^>]*>\s*(.+?)\s*</div>', html_content, re.DOTALL)
    if pm_match:
        return pm_match.group(1).strip()
    return None


def extract_description_from_html(html_content):
    """Extract description from HTML."""
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', html_content)
    if desc_match and desc_match.group(1).strip():
        return desc_match.group(1).strip()
    p_match = re.search(r'</h1>\s*<p[^>]*>\s*(.+?)\s*</p>', html_content, re.DOTALL)
    if p_match:
        desc = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()
        if len(desc) > 200:
            desc = desc[:197] + '...'
        return desc if desc else None
    return None


def try_parse_date(date_str):
    """Try to parse a date string into a datetime object for sorting.
    Returns the datetime or None."""
    if not date_str or date_str == 'Unknown Date':
        return None
    formats = [
        '%d %b %Y',      # 29 Apr 2026
        '%b %d, %Y',     # Mar 31, 2026 / Sep 2, 2025
        '%B %d, %Y',     # March 31, 2026
        '%Y-%m-%d',      # 2026-04-29
        '%d/%m/%Y',      # 29/04/2026
        '%d-%m-%Y',      # 29-04-2026
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None


def read_existing_blogs_html():
    """Parse existing blogs.html to extract per-folder metadata (title, date, overview)."""
    existing = {}
    blogs_path = Path('blogs.html')
    if not blogs_path.exists():
        return existing

    with open(blogs_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all blog-preview blocks
    blocks = re.split(r'<article class="blog-preview">', content)[1:]
    for block in blocks:
        end = block.find('</article>')
        if end == -1:
            continue
        block = block[:end]

        # Extract folder name from href (blog/.../index.html or external LinkedIn URL)
        href_m = re.search(r'href="(blog/([^"]+)/index\.html|https://www\.linkedin\.com/[^"]+)"', block)
        if not href_m:
            continue
        if href_m.group(1).startswith('http'):
            # External LinkedIn link — derive key from title text
            title_m = re.search(r'<a[^>]*>\s*(.+?)\s*</a>', block, re.DOTALL)
            if title_m:
                folder_name = title_m.group(1).strip()
                folder_name = re.sub(r'\s+', ' ', folder_name)
            else:
                continue
        else:
            folder_name = href_m.group(2).strip()

        # Extract title between <a> tags
        title_m = re.search(r'<a[^>]*>\s*(.+?)\s*</a>', block, re.DOTALL)
        title = title_m.group(1).strip() if title_m else 'Untitled'
        # Collapse whitespace in multi-line titles
        title = re.sub(r'\s+', ' ', title)

        # Extract date from post-meta
        date_m = re.search(r'<div class="post-meta">(.+?)</div>', block, re.DOTALL)
        date = date_m.group(1).strip() if date_m else 'Unknown Date'

        # Extract overview from <p>
        overview_m = re.search(r'<p>(.*?)</p>', block, re.DOTALL)
        overview = overview_m.group(1).strip() if overview_m else 'No description available'
        overview = re.sub(r'\s+', ' ', overview)

        existing[folder_name] = {
            'title': title,
            'date': date,
            'overview': overview,
        }
        # Preserve external LinkedIn URL if present
        ext_m = re.search(r'href="(https://www\.linkedin\.com/[^"]+)"', block)
        if ext_m:
            existing[folder_name]['external_url'] = ext_m.group(1)

    return existing


def scan_blog_html_files():
    """Scan all blog/*/index.html files and extract metadata.
    Preserves existing metadata from blogs.html; falls back to .md / HTML extraction."""
    blog_dir = Path('blog')
    entries = []

    if not blog_dir.exists():
        print("Blog directory not found!")
        return entries

    # Read existing blogs.html to preserve manually curated metadata
    existing_meta = read_existing_blogs_html()

    # Collect dates/descriptions/titles from .md files (YAML frontmatter)
    md_dates = {}
    md_descriptions = {}
    md_titles = {}
    for folder in blog_dir.iterdir():
        if not folder.is_dir() or folder.name == '__pycache__':
            continue
        for file in folder.iterdir():
            if file.suffix == '.md':
                date, overview, _, _, frontmatter_title = extract_metadata_from_md(file)
                if date and date != 'Unknown Date':
                    md_dates[folder.name] = date
                if overview and overview != 'No description available':
                    md_descriptions[folder.name] = overview
                if frontmatter_title:
                    md_titles[folder.name] = frontmatter_title
                break

    # Scan all index.html files
    for folder in sorted(blog_dir.iterdir()):
        if not folder.is_dir() or folder.name == '__pycache__':
            continue

        index_path = folder / 'index.html'
        if not index_path.exists():
            continue

        fn = folder.name

        # 1. Prefer existing blogs.html data (manually curated)
        if fn in existing_meta:
            meta = existing_meta[fn]
            date = meta['date']
            title = meta['title']
            overview = meta['overview']
            entry = {
                'folder_name': fn,
                'title': title,
                'date': date,
                'overview': overview,
                'date_obj': try_parse_date(date),
            }
            if 'external_url' in meta:
                entry['external_url'] = meta['external_url']
            entries.append(entry)
            continue

        # 2. Extract from HTML
        with open(index_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        title = md_titles.get(fn) or extract_title_from_html(html_content)
        date = extract_date_from_html(html_content)
        if not date or date == 'Unknown Date':
            date = md_dates.get(fn, 'Unknown Date')
        if not date:
            date = 'Unknown Date'

        description = extract_description_from_html(html_content)
        if not description or description == 'No description available':
            description = md_descriptions.get(fn, 'No description available')
        if not description:
            description = 'No description available'

        entries.append({
            'folder_name': fn,
            'title': title,
            'date': date,
            'overview': description,
            'date_obj': try_parse_date(date),
        })

    return entries


def update_blogs_html(blog_entries):
    """Rebuild blogs.html with all blog entries from scratch."""
    with open('blogs.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the content div boundaries
    content_start = content.find('<div class="content">')
    rest_start = content.find('\n    <script', content_start)

    if content_start == -1 or rest_start == -1:
        rest_start = content.find('\n\n    <script', content_start)
    if content_start == -1 or rest_start == -1:
        print("Could not find content section in blogs.html")
        return

    # Sort by date: newest first, Unknown Date at end
    def sort_key(entry):
        dt = entry.get('date_obj')
        if dt:
            return (0, dt)
        return (1, datetime.min)

    sorted_entries = sorted(blog_entries, key=sort_key, reverse=True)
    entries_html = ''
    for entry in sorted_entries:
        folder_name = entry['folder_name']
        title = entry['title']
        date = entry['date']
        overview = entry['overview']
        external_url = entry.get('external_url', '')
        if external_url:
            href = f'{external_url}" target="_blank" rel="noopener'
        else:
            href = f'blog/{folder_name}/index.html'
        entries_html += f'''            <article class="blog-preview">
                <h2><a href="{href}">{title}</a></h2> 
                <div class="post-meta">{date}</div>
                <p>{overview}</p>
            </article>

'''

    insertion_point = content_start + len('<div class="content">\n')
    new_content = (content[:insertion_point] + entries_html + content[rest_start:])

    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Regenerated blogs.html with {len(blog_entries)} entries")


# ─── Main ────────────────────────────────────────────────────────────────

def main():
    """Main function: process .md files → index.html, then rebuild blogs.html."""
    print("Starting blog generation process...")

    # Step 1: Process markdown files (regenerate index.html for posts with .md source)
    md_files = find_md_files_in_blog_folders()
    if md_files:
        print(f"Found {len(md_files)} markdown files to process.")
        for md_file in md_files:
            print(f"Processing {md_file}...")

            date, overview, is_private, cleaned_content, frontmatter_title = extract_metadata_from_md(md_file)

            # Get title: from frontmatter first, then from # Heading, then from filename
            title_from_heading = None
            if frontmatter_title:
                title = frontmatter_title
            else:
                title_match = re.search(r'^#\s*(.+)$', cleaned_content, re.MULTILINE)
                title_from_heading = title_match.group(1).strip() if title_match else None
                title = title_from_heading if title_from_heading else md_file.stem

            if title_from_heading:
                cleaned_content = re.sub(r'^#\s*.+$', '', cleaned_content, count=1, flags=re.MULTILINE)
                cleaned_content = cleaned_content.strip()

            html_content = convert_md_to_html(cleaned_content, title)
            html_output = create_html_from_template(title, html_content, md_file.parent.name, is_private)

            output_path = md_file.parent / 'index.html'
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_output)

            print(f"Generated {output_path}")
    else:
        print("No markdown files found in blog folders.")

    # Step 2: Scan all blog index.html files and rebuild blogs.html
    print("\nScanning blog HTML files to rebuild blogs.html...")
    blog_entries = scan_blog_html_files()
    if blog_entries:
        update_blogs_html(blog_entries)
    else:
        print("No blog entries found.")

    print("Blog generation completed!")


if __name__ == "__main__":
    main()
