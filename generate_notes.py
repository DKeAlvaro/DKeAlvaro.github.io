import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

def extract_overview_and_keywords(md_file_path):
    """Extract the overview text and keywords from a markdown file."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Look for 'Overview:' followed by text
            overview_match = re.search(r'Overview:\s*(.+?)(?=\n\n|\n#|\nKeywords:|$)', content, re.DOTALL)
            overview = overview_match.group(1).strip() if overview_match else None
            
            # Look for 'Keywords:' followed by text
            keywords_match = re.search(r'Keywords:\s*(.+?)(?=\n\n|\n#|$)', content, re.DOTALL)
            keywords = keywords_match.group(1).strip() if keywords_match else None
            
            return overview, keywords
    except Exception as e:
        print(f"Error reading {md_file_path}: {e}")
    return None, None

def extract_overview_and_date(md_file_path):
    """Extract the overview text and date from a markdown file."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Look for 'Overview:' followed by text
            overview_match = re.search(r'Overview:\s*(.+?)(?=\n\n|\n#|\nDate:|$)', content, re.DOTALL)
            overview = overview_match.group(1).strip() if overview_match else None
            
            # Look for 'Date:' followed by text
            date_match = re.search(r'Date:\s*(.+?)(?=\n\n|\n#|$)', content, re.DOTALL)
            date = date_match.group(1).strip() if date_match else None
            
            return overview, date
    except Exception as e:
        print(f"Error reading {md_file_path}: {e}")
    return None, None

def run_html_generator():
    """Run the generate_html.py script in the notes directory."""
    print("\n🔄 Running HTML generator...")
    
    notes_dir = Path('./notes')
    html_generator = notes_dir / 'generate_html.py'
    
    if not html_generator.exists():
        print(f"❌ HTML generator not found at {html_generator}")
        return False
    
    try:
        # Change to notes directory and run the script
        original_cwd = Path.cwd()
        os.chdir(notes_dir)
        
        # Run the HTML generator script
        result = subprocess.run([sys.executable, 'generate_html.py'], 
                              capture_output=True, text=True, check=True)
        
        print("✅ HTML generation completed successfully!")
        if result.stdout:
            print("HTML Generator Output:")
            print(result.stdout)
        
        # Change back to original directory
        os.chdir(original_cwd)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ HTML generation failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        os.chdir(original_cwd)
        return False
    except Exception as e:
        print(f"❌ Error running HTML generator: {e}")
        os.chdir(original_cwd)
        return False

def get_notes_entries():
    """Scan the notes directory and collect all note entries."""
    notes_dir = Path('./notes')
    entries = []
    
    if not notes_dir.exists():
        print("Notes directory not found!")
        return entries
    
    # Scan each subdirectory in notes
    for subdir in notes_dir.iterdir():
        if subdir.is_dir() and subdir.name != '__pycache__':
            # Look for .md files in the subdirectory
            md_files = list(subdir.glob('*.md'))
            if md_files:
                # Use the first .md file found
                md_file = md_files[0]
                overview, date = extract_overview_and_date(md_file)
                
                if overview:
                    # Create relative path for the HTML link (not markdown)
                    html_filename = md_file.stem + '.html'
                    relative_path = f"notes/{subdir.name}/{html_filename}"
                    
                    entries.append({
                        'title': subdir.name.replace('_', ' '),
                        'path': relative_path,
                        'overview': overview,
                        'date': date,
                        'folder': subdir.name
                    })
    
    # Sort entries alphabetically by title
    entries.sort(key=lambda x: x['title'])
    return entries

def generate_notes_html(entries):
    """Generate the complete notes.html content."""
    # Generate entries HTML first
    entries_html = ""
    for entry in entries:
        # Use date if available, otherwise fall back to folder name
        meta_text = entry['date'] if entry['date'] else f"{entry['folder']} • Study Notes"
        
        entries_html += f'''                <div class="notes-chapter">
                    <h2 class="chapter-title"><a href="{entry['path']}">{entry['title']}</a></h2>
                    <div class="chapter-meta">{meta_text}</div>
                    <p class="chapter-description">{entry['overview']}</p>
                </div>

'''
    
    # HTML template with entries already inserted
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
        .notes-chapter {{
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5rem;
        }}
        .notes-chapter:last-child {{
            border-bottom: none;
        }}
        .chapter-title {{
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
            color: var(--primary-color);
            font-weight: 500;
        }}
        .chapter-meta {{
            font-size: 0.9rem;
            color: var(--text-color);
            opacity: 0.7;
            margin-bottom: 0.8rem;
        }}
        .chapter-description {{
            color: var(--text-color);
            line-height: 1.6;
            margin-bottom: 0;
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
    print("🚀 Starting notes generation process...")
    
    # Step 1: Run HTML generator first
    html_success = run_html_generator()
    
    if not html_success:
        print("⚠️  HTML generation failed, but continuing with notes.html generation...")
    
    # Step 2: Generate notes.html with correct links
    print("\n📝 Scanning notes directory...")
    entries = get_notes_entries()
    
    if not entries:
        print("❌ No notes found with 'Overview:' text!")
        return 1
    
    print(f"Found {len(entries)} note entries:")
    for entry in entries:
        date_info = f" (Date: {entry['date']})" if entry['date'] else " (No date found)"
        print(f"  - {entry['title']}{date_info}")
        print(f"    → Links to: {entry['path']}")
    
    print("\n🔨 Generating notes.html...")
    html_content = generate_notes_html(entries)
    
    # Write the HTML file
    try:
        with open('notes.html', 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print("✅ notes.html generated successfully!")
        print(f"🕒 Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if html_success:
            print("\n🎉 Complete process finished successfully!")
            print("   - HTML files generated from Markdown")
            print("   - notes.html updated with correct HTML links")
        else:
            print("\n⚠️  Process completed with warnings:")
            print("   - notes.html generated successfully")
            print("   - HTML generation had issues (check above)")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error writing notes.html: {e}")
        return 1

if __name__ == "__main__":
    exit(main())