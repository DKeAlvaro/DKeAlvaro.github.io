import os
import re
import yaml
from datetime import datetime
import markdown
from pathlib import Path

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
    # Convert markdown to HTML
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

def update_blogs_html(blog_entries):
    """Update blogs.html with new blog entries"""
    with open('blogs.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the content div where blog entries are added
    content_start = content.find('<div class="content">')
    content_end = content.find('</div>\n    </div>\n    <script')
    
    if content_start == -1 or content_end == -1:
        # Try another common pattern
        content_end = content.find('</div>\n    </div>\n\n    <script')
        
    if content_start == -1 or content_end == -1:
        print("Could not find content section in blogs.html")
        return
    
    # Extract existing entries to avoid duplicates
    existing_content = content[content_start:content_end]
    
    # Build new entries HTML
    new_entries_html = ''
    for entry in blog_entries:
        folder_name = entry['folder_name']
        title = entry['title']
        date = entry['date']
        overview = entry['overview']
        
        # Check if entry already exists
        if f'href="blog/{folder_name}/index.html"' not in existing_content:
            entry_html = f'''            <article class="blog-preview">
                <h2><a href="blog/{folder_name}/index.html">{title}</a></h2> 
                <div class="post-meta">{date}</div>
                <p>{overview}</p>
            </article>

'''
            new_entries_html += entry_html
    
    if new_entries_html:
        # Insert new entries at the beginning of content
        insertion_point = content_start + len('<div class="content">\n')
        new_content = (content[:insertion_point] + 
                      new_entries_html + 
                      content[insertion_point:])
        
        # Write updated content
        with open('blogs.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added {len(blog_entries)} new blog entries to blogs.html")
    else:
        print("No new entries to add to blogs.html")

def main():
    """Main function to process all markdown files"""
    print("Starting blog generation process...")
    
    # Find all markdown files
    md_files = find_md_files_in_blog_folders()
    
    if not md_files:
        print("No markdown files found in blog folders.")
        return
    
    print(f"Found {len(md_files)} markdown files to process.")
    
    blog_entries = []
    
    for md_file in md_files:
        print(f"Processing {md_file}...")
        
        # Extract metadata and clean content
        date, overview, is_private, cleaned_content, frontmatter_title = extract_metadata_from_md(md_file)

        # Get title: from frontmatter first, then from # Heading, then from filename
        title_from_heading = None
        if frontmatter_title:
            title = frontmatter_title
        else:
            title_match = re.search(r'^#\s*(.+)$', cleaned_content, re.MULTILINE)
            title_from_heading = title_match.group(1).strip() if title_match else None
            title = title_from_heading if title_from_heading else md_file.stem

        # Remove the title line from content to avoid duplication (only if it came from heading)
        if title_from_heading:
            cleaned_content = re.sub(r'^#\s*.+$', '', cleaned_content, count=1, flags=re.MULTILINE)
            cleaned_content = cleaned_content.strip()
        
        # Convert to HTML
        html_content = convert_md_to_html(cleaned_content, title)
        
        # Create HTML file using template
        html_output = create_html_from_template(title, html_content, md_file.parent.name, is_private)
        
        # Write HTML file
        output_path = md_file.parent / 'index.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)
        
        print(f"Generated {output_path}")
        
        # Add to blog entries list
        blog_entries.append({
            'folder_name': md_file.parent.name,
            'title': title,
            'date': date,
            'overview': overview
        })
    
    # Update blogs.html
    if blog_entries:
        update_blogs_html(blog_entries)
    
    print("Blog generation completed!")

if __name__ == "__main__":
    main()