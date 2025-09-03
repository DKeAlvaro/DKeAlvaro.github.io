import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

def extract_overview_and_date(md_file_path):
    """Extract the overview text and date from a markdown file."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            overview_match = re.search(r'Overview:\s*(.+?)(?=\n\n|\n#|\nDate:|$)', content, re.DOTALL)
            overview = overview_match.group(1).strip() if overview_match else None
            
            date_match = re.search(r'Date:\s*(.+?)(?=\n\n|\n#|$)', content, re.DOTALL)
            date = date_match.group(1).strip() if date_match else None
            
            return overview, date
    except Exception as e:
        print(f"Error reading {md_file_path}: {e}")
    return None, None

def run_html_generator():
    """Run the generate_html.py script in the notes directory."""
    print("\nRunning HTML generator...")
    
    notes_dir = Path('./notes')
    html_generator = notes_dir / 'generate_html.py'
    
    if not html_generator.exists():
        print(f"HTML generator not found at {html_generator}")
        return False
    
    try:
        original_cwd = Path.cwd()
        os.chdir(notes_dir)
        
        result = subprocess.run([sys.executable, 'generate_html.py'], 
                              capture_output=True, text=True, check=True)
        
        print("HTML generation completed successfully!")
        if result.stdout:
            print("HTML Generator Output:")
            print(result.stdout)
        
        os.chdir(original_cwd)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"HTML generation failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        os.chdir(original_cwd)
        return False
    except Exception as e:
        print(f"Error running HTML generator: {e}")
        os.chdir(original_cwd)
        return False

def get_all_md_files(directory):
    """Scan a directory recursively and return a list of all markdown files."""
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    return md_files

def build_tree_from_files(files):
    """Build a nested dictionary from a list of markdown files."""
    tree = {'files': [], 'folders': {}}
    for file in files:
        parts = file.relative_to('notes').parts
        current_level = tree
        for part in parts[:-1]:
            current_level = current_level['folders'].setdefault(part, {'files': [], 'folders': {}})
        
        overview, date = extract_overview_and_date(file)
        if overview:
            html_filename = file.stem + '.html'
            absolute_file_path = file.resolve()
            relative_path = absolute_file_path.relative_to(Path.cwd()).with_suffix('.html')
            current_level['files'].append({
                'title': file.stem.replace('_', ' '),
                'path': str(relative_path).replace('\\', '/'),
                'overview': overview,
                'date': date
            })
    return tree

def generate_tree_html(tree):
    """Generate HTML for the notes tree."""
    html = '<ul class="notes-tree-level">\n'
    for file in tree['files']:
        meta_text = file['date'] if file['date'] else ""
        html += f'''<li class="tree-file">
<div class="tree-file-content">
    <a href="{file['path']}">{file['title']}</a>
    <p class="tree-file-description">{file['overview']}</p>
</div>
<div class="tree-file-meta">{meta_text}</div>
</li>
'''
    for folder_name, folder_content in tree['folders'].items():
        if not folder_content['folders']:
            for file in folder_content['files']:
                meta_text = file['date'] if file['date'] else ""
                html += f'''<li class="tree-file">
<div class="tree-file-content">
    <a href="{file['path']}">{file['title']}</a>
    <p class="tree-file-description">{file['overview']}</p>
</div>
<div class="tree-file-meta">{meta_text}</div>
</li>
'''
        else:
            html += f'<li class="tree-folder"><span>{folder_name.replace('_', ' ')}</span>\n'
            html += generate_tree_html(folder_content)
            html += '</li>\n'
    html += '</ul>\n'
    return html

def generate_notes_html(tree):
    """Generate the complete notes.html content."""
    entries_html = generate_tree_html(tree)
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Alvaro Menendez's MSc AI & Engineering Systems notes and study materials">
    <title>MSc AIES - Alvaro Menendez</title>
    <link rel="icon" href="./assets/svg/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="styles.css">
    <style>
        .notes-index {{
            max-width: 800px;
            margin: 0 auto;
        }}
        .notes-header {{
            text-align: center;
            margin-top: 4rem;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 2px solid var(--border-color);
        }}
        .notes-header h1 {{
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
        }}
        .notes-subtitle {{
            font-size: 1.1rem;
            color: var(--text-color);
            opacity: 0.8;
            font-weight: 400;
        }}
        .notes-tree-level {{
            list-style: none;
            padding-left: 0;
        }}
        .notes-tree-level ul {{
            padding-left: 1rem;
            margin-left: 0;
            border-left: 2px solid var(--border-color);
            margin-top: 0.5rem;
        }}
        .tree-folder {{
            cursor: pointer;
        }}
        .tree-folder > span {{
            font-weight: 600;
            font-size: 1.1rem;
            color: var(--primary-color);
            display: block;
            margin-top: 1.2rem;
            margin-bottom: 0.8rem;
            padding: 0.3rem 0;
            border-radius: 4px;
            transition: background-color 0.2s ease;
        }}
        .tree-folder > span:hover {{
            background-color: var(--light-gray);
            padding-left: 0.5rem;
        }}
        .tree-folder > span::before {{
            content: '▼';
            margin-right: 8px;
            display: inline-block;
            width: 12px;
            font-size: 0.8rem;
            transition: transform 0.2s ease;
        }}
        .tree-folder.collapsed > span::before {{
             content: '▶';
             transform: none;
         }}
         .tree-folder.collapsed > ul,
         .notes-tree-level ul.collapsed {{
             display: none;
         }}
         .tree-file {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0.8rem 0;
            border-bottom: 1px solid var(--border-color);
            margin-left: 0.5rem;
        }}
        .tree-file:last-child {{
            border-bottom: none;
        }}
        .tree-file-content a {{
            font-size: 1rem;
            color: var(--accent-color);
            font-weight: 500;
            text-decoration: none;
        }}
        .tree-file-content a:hover {{
            text-decoration: underline;
        }}
        .tree-file-description {{
            font-size: 0.85rem;
            color: var(--text-color);
            opacity: 0.8;
            margin-top: 0.2rem;
            margin-bottom: 0;
        }}
        .tree-file-meta {{
            font-size: 0.8rem;
            color: var(--text-color);
            opacity: 0.6;
            white-space: nowrap;
            padding-left: 1rem;
        }}
    </style>
</head>
<body>
    <div class="menu-overlay"></div>
    <header>
        <nav class="nav-container">
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <ul class="nav-links" id="navLinks">
                <li><a href="./index.html">About</a></li>
                <li><a href="./journey.html">My Life</a></li>
                <li><a href="./projects.html">Projects</a></li>
                <li><a href="./blogs.html">Blog</a></li>
                <li><a href="./notes.html">MSc AIES</a></li>
                <li><a href="https://dailyclips.es/" target="_blank">Daily Clips</a></li>
                <li><a href="https://alvaromenendez.es/ufc-predictions/" target="_blank">UFC Predictions</a></li>
                <li><a href="./acknowledgments.html">Acknowledgments</a></li>
                <li><a href="./assets/Alvaro_Menendez_CV.pdf" download>CV</a></li>
            </ul>
            <div class="nav-right">
                <div class="social-links">
                    <a href="https://github.com/DKeAlvaro" target="_blank" aria-label="GitHub">
                        <img src="assets/svg/github.svg" alt="GitHub" class="social-icon">
                    </a>
                    <a href="https://www.linkedin.com/in/alvaromenendezros" target="_blank" aria-label="LinkedIn">
                        <img src="assets/svg/linkedin.svg" alt="LinkedIn" class="social-icon">
                    </a>
                    <a href="mailto:alvaro.mrgr2@gmail.com" aria-label="Email">
                        <img src="assets/svg/gmail.svg" alt="Email" class="social-icon">
                    </a>
                </div>
                <div class="theme-toggle" id="themeToggle" aria-label="Toggle theme" role="button" tabindex="0"><img src="assets/svg/sun.svg" alt="Toggle theme" class="theme-icon"></div>
            </div>
        </nav>
    </header>

    <div class="page-container">
        <div class="content">
            <div class="notes-header">
                <h1>MSc AI & Engineering Systems</h1>
                <p class="notes-subtitle">Study Notes & Materials • TU/e</p>
            </div>
            
            <div class="notes-index">
{entries_html.rstrip()}
            </div>
        </div>
    </div>

    <footer>
        <p id="footerYear"></p>
    </footer>

    <script src="./script.js"></script>
</body>
</html>'''
    
    return html_content

def main():
    """Main function to generate notes.html and run HTML generator."""
    print("Starting notes generation process...")
    
    html_success = run_html_generator()
    
    if not html_success:
        print("HTML generation failed, but continuing with notes.html generation...")
    
    print("\nScanning notes directory...")
    md_files = get_all_md_files('./notes')
    notes_tree = build_tree_from_files(md_files)
    
    if not notes_tree:
        print("No notes found!")
        return 1
    
    print(f"Found notes and folders. Building tree structure.")
    
    print("\nGenerating notes.html...")
    html_content = generate_notes_html(notes_tree)
    
    try:
        with open('notes.html', 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print("notes.html generated successfully!")
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if html_success:
            print("\nComplete process finished successfully!")
            print("   - HTML files generated from Markdown")
            print("   - notes.html updated with correct HTML links")
        else:
            print("\nProcess completed with warnings:")
            print("   - notes.html generated successfully")
            print("   - HTML generation had issues (check above)")
        
        return 0
        
    except Exception as e:
        print(f"Error writing notes.html: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
