import os
import re
from pathlib import Path
from datetime import datetime
import markdown

def convert_md_to_html(md_file_path, output_dir):
    """Convert a markdown file to HTML with proper styling and navigation."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()
        
        # Extract title from filename or first heading
        title = md_file_path.stem.replace('_', ' ')
        
        # Remove overview and date lines from content
        md_content = re.sub(r'^Overview:.*$', '', md_content, flags=re.MULTILINE)
        md_content = re.sub(r'^Date:.*$', '', md_content, flags=re.MULTILINE)
        
        # Convert markdown to HTML with HTML preservation
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'], extension_configs={
            'extra': {
                'markdown.extensions.extra': {
                    'safe_mode': False
                }
            }
        })
        
        # Generate complete HTML page
        full_html = generate_complete_html(title, html_content)
        
        # Create output file path
        output_file = output_dir / f"{md_file_path.stem}.html"
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(full_html)
        
        print(f"Generated: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error converting {md_file_path}: {e}")
        return False

def generate_complete_html(title, content):
    """Generate a complete HTML page with navigation and styling."""
    
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - MSc AI & Engineering Systems Notes">
    <title>{title} - MSc AIES</title>
    <link rel="icon" href="../../assets/svg/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="../../styles.css">
    <style>
        .note-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .note-header {{
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 2px solid var(--border-color);
        }}
        .note-title {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 0rem;
            padding: 0.3rem 0.6rem;
            color: var(--text-color);
            text-decoration: none;
            font-size: 0.9rem;
            border: 1px solid var(--border-color);
            border-radius: 4px;
            transition: color 0.2s ease;
        }}
        .back-link:hover {{
            color: var(--primary-color);
        }}
        .note-content {{
            line-height: 1.8;
            color: var(--text-color);
        }}
        .note-content h1, .note-content h2, .note-content h3 {{
            color: var(--primary-color);
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}
        .note-content img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 1rem 0;
            display: block;
        }}
        /* Preserve centered images from markdown HTML */
        .note-content div[style*="text-align: center"] {{
            text-align: center !important;
        }}
        .note-content div[style*="text-align: center"] img {{
            margin: 1rem auto;
        }}
        .note-content pre {{
            background: var(--code-bg);
            padding: 1rem;
            border-radius: 5px;
            overflow-x: auto;
        }}
        .note-content code {{
            background: var(--code-bg);
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        .note-content blockquote {{
            border-left: 4px solid var(--primary-color);
            padding-left: 1rem;
            margin: 1rem 0;
            font-style: italic;
            opacity: 0.9;
        }}
        .note-content ul, .note-content ol {{
            padding-left: 2rem;
        }}
        .note-content li {{
            margin-bottom: 0.5rem;
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
                <li><a href="../../index.html">About</a></li>
                <li><a href="../../journey.html">My Life</a></li>
                <li><a href="../../projects.html">Projects</a></li>
                <li><a href="../../blogs.html">Blog</a></li>
                <li><a href="../../notes.html">MSc AIES</a></li>
                <li><a href="https://dailyclips.es/" target="_blank">Daily Clips</a></li>
                <li><a href="https://alvaromenendez.es/ufc-predictions/" target="_blank">UFC Predictions</a></li>
                <li><a href="../../acknowledgments.html">Acknowledgments</a></li>
                <li><a href="../../assets/Alvaro_Menendez_CV.pdf" download>CV</a></li>
            </ul>
            <div class="nav-right">
                <div class="social-links">
                    <a href="https://github.com/DKeAlvaro" target="_blank" aria-label="GitHub">
                        <img src="../../assets/svg/github.svg" alt="GitHub" class="social-icon">
                    </a>
                    <a href="https://www.linkedin.com/in/alvaromenendezros" target="_blank" aria-label="LinkedIn">
                        <img src="../../assets/svg/linkedin.svg" alt="LinkedIn" class="social-icon">
                    </a>
                    <a href="mailto:alvaro.mrgr2@gmail.com" aria-label="Email">
                        <img src="../../assets/svg/gmail.svg" alt="Email" class="social-icon">
                    </a>
                </div>
                <div class="theme-toggle" id="themeToggle" aria-label="Toggle theme" role="button" tabindex="0">
                    <img src="../../assets/svg/sun.svg" alt="Toggle theme" class="theme-icon" id="themeIcon">
                </div>
            </div>
        </nav>
    </header>

    <div class="page-container">
        <div class="content">
            <div class="note-container">
                <a href="../../notes.html" class="back-link">← Back to Notes</a>
                                
                <div class="note-content">
                    {content}
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p id="footerYear"></p>
    </footer>

    <script src="../../script.js"></script>
</body>
</html>'''
    
    return html_template

def process_notes_directory():
    """Process all markdown files in the notes directory structure."""
    notes_dir = Path('.')
    processed_files = 0
    failed_files = 0
    
    print("Scanning notes directory for Markdown files...")
    
    # Process each subdirectory
    for subdir in notes_dir.iterdir():
        if subdir.is_dir() and subdir.name != '__pycache__':
            print(f"\nProcessing folder: {subdir.name}")
            
            # Find all .md files in the subdirectory
            md_files = list(subdir.glob('*.md'))
            
            if not md_files:
                print(f"   No Markdown files found in {subdir.name}")
                continue
            
            # Process each markdown file
            for md_file in md_files:
                print(f"   Converting: {md_file.name}")
                
                if convert_md_to_html(md_file, subdir):
                    processed_files += 1
                else:
                    failed_files += 1
    
    # Summary
    print(f"\n{'='*50}")
    print(f"CONVERSION SUMMARY")
    print(f"{'='*50}")
    print(f"Successfully converted: {processed_files} files")
    if failed_files > 0:
        print(f"Failed conversions: {failed_files} files")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

def main():
    """Main function to run the HTML generation process."""
    print("Starting Markdown to HTML conversion...")
    print(f"Working directory: {Path.cwd()}")
    
    # Check if we're in the notes directory
    if not Path.cwd().name == 'notes':
        print("Warning: This script should be run from the 'notes' directory")
        print("   Current directory:", Path.cwd())
        response = input("   Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborted by user")
            return 1
    
    try:
        process_notes_directory()
        print("\nHTML generation completed successfully!")
    except Exception as e:
        print(f"\nFatal error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())