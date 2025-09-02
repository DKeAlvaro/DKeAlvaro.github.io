import os
import re
from pathlib import Path
from datetime import datetime
import markdown

def process_qa_content(md_content):
    """Process Q&A patterns in markdown content and convert them to collapsible HTML."""
    # Pattern to match Q: ... followed by A: ... (each on their own lines)
    qa_pattern = r'^Q:\s*(.+?)\n^A:\s*(.+?)(?=\n\n|\n^Q:|\n^[^A]|$)'
    
    def replace_qa(match):
        question = match.group(1).strip()
        answer = match.group(2).strip()
        
        # Generate unique ID for each Q&A pair
        qa_id = f"qa-{hash(question) % 10000}"
        
        return f'''<div class="qa-item">
    <div class="qa-question" onclick="toggleQA('{qa_id}')">
        <span class="qa-icon">▶</span>
        <span class="qa-text">{question}</span>
    </div>
    <div class="qa-answer" id="{qa_id}">
        {answer}
    </div>
</div>'''
    
    # Replace Q&A patterns with HTML
    processed_content = re.sub(qa_pattern, replace_qa, md_content, flags=re.MULTILINE | re.DOTALL)
    
    return processed_content

def convert_md_to_html(md_file_path, output_dir, path_prefix):
    """Convert a markdown file to HTML with proper styling and navigation."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()
        
        # Extract title from filename
        title = md_file_path.stem.replace('_', ' ').replace('-', ' ').title()
        
        # Remove overview and date lines from content
        md_content = re.sub(r'^Overview:.*$', '', md_content, flags=re.MULTILINE)
        md_content = re.sub(r'^Date:.*$', '', md_content, flags=re.MULTILINE)
        
        # Process Q&A patterns before markdown conversion
        md_content = process_qa_content(md_content)
        
        # Convert markdown to HTML with extensions
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'fenced_code', 'tables'])
        
        # Generate complete HTML page using the calculated path prefix
        full_html = generate_complete_html(title, html_content, path_prefix)
        
        # Create output file path
        output_file = output_dir / f"{md_file_path.stem}.html"
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(full_html)
        
        return True
        
    except Exception as e:
        print(f"    -> Error converting {md_file_path.name}: {e}")
        return False

def generate_complete_html(title, content, path_prefix):
    """Generate a complete HTML page with dynamic paths for navigation and styling."""
    
    # The HTML template now uses 'path_prefix' to dynamically set the correct relative paths
    # for assets, stylesheets, and navigation links.
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - MSc AI & Engineering Systems Notes">
    <title>{title} - MSc AIES</title>
    <link rel="icon" href="{path_prefix}assets/svg/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="{path_prefix}styles.css">
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
        
        /* Q&A Styles */
        .qa-item {{
            margin: 1.5rem 0;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            overflow: hidden;
            background: var(--bg-color);
        }}
        
        .qa-question {{
            padding: 1rem;
            background: var(--secondary-bg, #f8f9fa);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            transition: background-color 0.2s ease;
            user-select: none;
        }}
        
        .qa-question:hover {{
            background: var(--hover-bg, #e9ecef);
        }}
        
        .qa-icon {{
            font-size: 0.8rem;
            transition: transform 0.2s ease;
            color: var(--primary-color);
            font-weight: bold;
        }}
        
        .qa-question.active .qa-icon {{
            transform: rotate(90deg);
        }}
        
        .qa-text {{
            font-weight: 600;
            color: var(--text-color);
            flex: 1;
        }}
        
        .qa-answer {{
            padding: 1rem;
            background: var(--bg-color);
            border-top: 1px solid var(--border-color);
            display: none;
            color: var(--text-color);
            line-height: 1.6;
        }}
        
        .qa-answer.active {{
            display: block;
        }}
        
        /* Mobile responsive styles */
        @media (max-width: 768px) {{
            .note-container {{
                padding: 0.5rem;
            }}
            .note-header {{
                margin-bottom: 1rem;
                padding-bottom: 1.5rem;
            }}
            .note-title {{
                font-size: 2rem;
            }}
            .note-content h1 {{
                font-size: 1.8rem;
            }}
            .note-content h2 {{
                font-size: 1.5rem;
            }}
            .note-content h3 {{
                font-size: 1.3rem;
            }}
            .note-content pre {{
                padding: 0.75rem;
                font-size: 0.9rem;
            }}
            .note-content ul, .note-content ol {{
                padding-left: 1.5rem;
            }}
        }}
        
        @media (max-width: 480px) {{
            .note-container {{
                padding: 0.5rem;
            }}
            .note-header {{
                margin-bottom: 1.15rem;
                padding-bottom: 0.75rem;
            }}
            .back-link {{
                padding: 0.25rem 0.5rem;
                font-size: 0.85rem;
            }}
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
                <li><a href="{path_prefix}index.html">About</a></li>
                <li><a href="{path_prefix}journey.html">My Life</a></li>
                <li><a href="{path_prefix}projects.html">Projects</a></li>
                <li><a href="{path_prefix}blogs.html">Blog</a></li>
                <li><a href="{path_prefix}notes.html">MSc AIES</a></li>
                <li><a href="https://dailyclips.es/" target="_blank">Daily Clips</a></li>
                <li><a href="https://alvaromenendez.es/ufc-predictions/" target="_blank">UFC Predictions</a></li>
                <li><a href="{path_prefix}acknowledgments.html">Acknowledgments</a></li>
                <li><a href="{path_prefix}assets/Alvaro_Menendez_CV.pdf" download>CV</a></li>
            </ul>
            <div class="nav-right">
                <div class="social-links">
                    <a href="https://github.com/DKeAlvaro" target="_blank" aria-label="GitHub">
                        <img src="{path_prefix}assets/svg/github.svg" alt="GitHub" class="social-icon">
                    </a>
                    <a href="https://www.linkedin.com/in/alvaromenendezros" target="_blank" aria-label="LinkedIn">
                        <img src="{path_prefix}assets/svg/linkedin.svg" alt="LinkedIn" class="social-icon">
                    </a>
                    <a href="mailto:alvaro.mrgr2@gmail.com" aria-label="Email">
                        <img src="{path_prefix}assets/svg/gmail.svg" alt="Email" class="social-icon">
                    </a>
                </div>
                <div class="theme-toggle" id="themeToggle" aria-label="Toggle theme" role="button" tabindex="0">
                    <img src="{path_prefix}assets/svg/moon.svg" alt="Toggle theme" class="theme-icon" id="themeIcon">
                </div>
            </div>
        </nav>
    </header>

    <div class="page-container">
        <div class="content">
            <div class="note-container">
                <a href="{path_prefix}notes.html" class="back-link">← Back to Notes</a>
                
                <div class="note-content">
                    {content}
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p id="footerYear"></p>
    </footer>

    <script src="{path_prefix}script.js"></script>
</body>
</html>'''
    
    return html_template

def process_notes_directory():
    """Process all markdown files in the notes directory structure recursively."""
    notes_dir = Path('.')
    processed_files = 0
    failed_files = 0
    
    print("Recursively scanning notes directory for Markdown files...")
    
    # Use glob('**/*.md') to find all markdown files in the current directory and all subdirectories
    md_files = list(notes_dir.glob('**/*.md'))
    
    if not md_files:
        print("No Markdown files found.")
        return

    for md_file in md_files:
        # Skip files in directories that should be ignored
        if any(part.startswith('.') or part == '__pycache__' for part in md_file.parts):
            continue

        # Determine the depth of the file to create the correct relative path prefix.
        # The number of parent directories in its relative path determines the depth.
        relative_path = md_file.relative_to(notes_dir)
        depth = len(relative_path.parent.parts)
        
        # The path prefix needs to go up 'depth' levels for the subdirectories,
        # plus one more level to get out of the 'notes' directory to the site root.
        path_prefix = '../' * (depth + 1)
        
        # The output directory is the same as the input file's directory
        output_dir = md_file.parent
        
        print(f"Processing: {relative_path}")
        
        # Pass the calculated prefix to the conversion function
        if convert_md_to_html(md_file, output_dir, path_prefix):
            processed_files += 1
            print(f" -> Generated: {output_dir / f'{md_file.stem}.html'}")
        else:
            failed_files += 1
            print(f" -> Failed: {relative_path}")
    
    # Summary
    print(f"\n{'='*50}")
    print(f"CONVERSION SUMMARY")
    print(f"{'='*50}")
    print(f"Successfully converted: {processed_files} files")
    if failed_files > 0:
        print(f"Failed conversions:   {failed_files} files")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

def main():
    """Main function to run the HTML generation process."""
    print("Starting Markdown to HTML conversion...")
    print(f"Working directory: {Path.cwd()}")
    
    # Check if we're in the notes directory
    if not Path.cwd().name == 'notes':
        print("\nWarning: This script is designed to be run from the 'notes' directory.")
        print(f"         Current directory: {Path.cwd()}")
        response = input("         Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborted by user.")
            return 1
    
    try:
        process_notes_directory()
        print("\nHTML generation completed!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())