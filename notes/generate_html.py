import os
import re
import json
from pathlib import Path
from datetime import datetime
import markdown
import subprocess
import sys

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

def convert_md_to_html(md_file_path, output_dir, path_prefix, folder_path=None):
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
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'fenced_code', 'tables', 'mdx_math'])
        
        # Generate complete HTML page using the calculated path prefix
        full_html = generate_complete_html(title, html_content, path_prefix, folder_path)
        
        # Create output file path
        output_file = output_dir / f"{md_file_path.stem}.html"
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(full_html)
        
        return True
        
    except Exception as e:
        print(f"    -> Error converting {md_file_path.name}: {e}")
        return False

def convert_ipynb_to_html(ipynb_file_path, output_dir, path_prefix, folder_path=None):
    """Convert a Jupyter notebook file to HTML with proper styling and navigation."""
    try:
        # Try to use nbconvert to convert the notebook
        try:
            # First, try using nbconvert command line tool
            result = subprocess.run([
                sys.executable, '-m', 'nbconvert', 
                '--to', 'html',
                '--template', 'basic',
                '--stdout',
                '--embed-images',  # Embed images as base64 in HTML
                '--no-prompt',     # Remove input prompts for cleaner output
                str(ipynb_file_path)
            ], capture_output=True, text=True, check=True)
            
            notebook_html = result.stdout
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            # If nbconvert is not available, try manual conversion
            print(f"    -> nbconvert not available, attempting manual conversion for {ipynb_file_path.name}")
            notebook_html = convert_ipynb_manually(ipynb_file_path)
        
        # Extract title from filename
        title = ipynb_file_path.stem.replace('_', ' ').replace('-', ' ').title()
        
        # Clean up the HTML content (remove HTML, HEAD, BODY tags if present)
        # Keep only the content inside the body
        body_match = re.search(r'<body[^>]*>(.*?)</body>', notebook_html, re.DOTALL | re.IGNORECASE)
        if body_match:
            content = body_match.group(1)
        else:
            content = notebook_html
        
        # Generate complete HTML page using the calculated path prefix
        full_html = generate_complete_html(title, content, path_prefix, folder_path)
        
        # Create output file path
        output_file = output_dir / f"{ipynb_file_path.stem}.html"
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(full_html)
        
        return True
        
    except Exception as e:
        print(f"    -> Error converting {ipynb_file_path.name}: {e}")
        return False

def convert_ipynb_manually(ipynb_file_path):
    """Manually convert a Jupyter notebook to basic HTML when nbconvert is not available."""
    try:
        with open(ipynb_file_path, 'r', encoding='utf-8') as file:
            notebook_data = json.load(file)
        
        html_content = []
        
        for cell in notebook_data.get('cells', []):
            cell_type = cell.get('cell_type', '')
            source = cell.get('source', [])
            
            if isinstance(source, list):
                source_text = ''.join(source)
            else:
                source_text = source
            
            if cell_type == 'markdown':
                # Convert markdown to HTML
                html_content.append('<div class="markdown-cell">')
                html_content.append(markdown.markdown(source_text, extensions=['extra', 'codehilite', 'fenced_code', 'tables']))
                html_content.append('</div>')
                
            elif cell_type == 'code':
                # Add code cell
                html_content.append('<div class="code-cell">')
                html_content.append('<div class="input-area">')
                html_content.append('<pre><code class="language-python">')
                html_content.append(source_text)
                html_content.append('</code></pre>')
                html_content.append('</div>')
                
                # Add output if present
                outputs = cell.get('outputs', [])
                if outputs:
                    html_content.append('<div class="output-area">')
                    for output in outputs:
                        if output.get('output_type') == 'stream':
                            text = ''.join(output.get('text', []))
                            html_content.append('<pre class="output-stream">')
                            html_content.append(text)
                            html_content.append('</pre>')
                        elif output.get('output_type') in ['execute_result', 'display_data']:
                            data = output.get('data', {})
                            
                            # Handle image outputs (PNG, JPEG, SVG)
                            if 'image/png' in data:
                                img_data = data['image/png']
                                if isinstance(img_data, list):
                                    img_data = ''.join(img_data)
                                html_content.append(f'<div class="output-image">')
                                html_content.append(f'<img src="data:image/png;base64,{img_data}" alt="Plot output" style="max-width: 100%; height: auto;" />')
                                html_content.append('</div>')
                            elif 'image/jpeg' in data:
                                img_data = data['image/jpeg']
                                if isinstance(img_data, list):
                                    img_data = ''.join(img_data)
                                html_content.append(f'<div class="output-image">')
                                html_content.append(f'<img src="data:image/jpeg;base64,{img_data}" alt="Plot output" style="max-width: 100%; height: auto;" />')
                                html_content.append('</div>')
                            elif 'image/svg+xml' in data:
                                svg_data = data['image/svg+xml']
                                if isinstance(svg_data, list):
                                    svg_data = ''.join(svg_data)
                                html_content.append(f'<div class="output-image">')
                                html_content.append(svg_data)
                                html_content.append('</div>')
                            elif 'text/html' in data:
                                # Handle HTML output (like pandas DataFrames)
                                html_data = data['text/html']
                                if isinstance(html_data, list):
                                    html_data = ''.join(html_data)
                                html_content.append('<div class="output-html">')
                                html_content.append(html_data)
                                html_content.append('</div>')
                            elif 'text/plain' in data:
                                text = data['text/plain']
                                if isinstance(text, list):
                                    text = ''.join(text)
                                html_content.append('<pre class="output-result">')
                                html_content.append(text)
                                html_content.append('</pre>')
                        elif output.get('output_type') == 'error':
                            # Handle error outputs
                            error_name = output.get('ename', 'Error')
                            error_value = output.get('evalue', '')
                            traceback = output.get('traceback', [])
                            
                            html_content.append('<div class="output-error">')
                            html_content.append(f'<pre class="error-name">{error_name}: {error_value}</pre>')
                            if traceback:
                                html_content.append('<pre class="error-traceback">')
                                for line in traceback:
                                    # Remove ANSI escape codes
                                    clean_line = re.sub(r'\x1b\[[0-9;]*m', '', line)
                                    html_content.append(clean_line)
                                html_content.append('</pre>')
                            html_content.append('</div>')
                    html_content.append('</div>')
                
                html_content.append('</div>')
        
        return '\n'.join(html_content)
        
    except Exception as e:
        print(f"    -> Error in manual conversion: {e}")
        return f"<p>Error converting notebook: {e}</p>"

def generate_complete_html(title, content, path_prefix, folder_path=None):
    """Generate a complete HTML page with dynamic paths for navigation and styling."""
    
    # Generate folder breadcrumb if folder_path is provided (excluding last folder)
    folder_breadcrumb = ""
    if folder_path and folder_path != Path('.'):
        folder_parts = folder_path.parts
        if len(folder_parts) > 1:  # Only show if there are parent folders
            # Exclude the last folder name
            parent_folders = folder_parts[:-1]
            folder_display = " / ".join(parent_folders)
            folder_breadcrumb = f'<span class="folder-path">{folder_display}</span>'
        elif len(folder_parts) == 1:
            # If only one folder level, show it
            folder_breadcrumb = f'<span class="folder-path">{folder_parts[0]}</span>'
    
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
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.js" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js" crossorigin="anonymous"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js" crossorigin="anonymous"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // Initialize KaTeX
            renderMathInElement(document.body, {{
                delimiters: [
                    {{left: "$$", right: "$$", display: true}},
                    {{left: "$", right: "$", display: false}}
                ]
            }});
            
            // Initialize Prism.js syntax highlighting
            if (typeof Prism !== 'undefined') {{
                Prism.highlightAll();
            }}
            
            // Handle theme switching for Prism.js
            function updatePrismTheme() {{
                const isDark = document.body.classList.contains('dark-theme');
                const prismLink = document.querySelector('link[href*="prism"]');
                if (prismLink) {{
                    if (isDark) {{
                        prismLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-dark.min.css';
                    }} else {{
                        prismLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css';
                    }}
                }}
            }}
            
            // Check initial theme
            updatePrismTheme();
            
            // Listen for theme changes
            const observer = new MutationObserver(function(mutations) {{
                mutations.forEach(function(mutation) {{
                    if (mutation.type === 'attributes' && mutation.attributeName === 'class') {{
                        updatePrismTheme();
                    }}
                }});
            }});
            
            observer.observe(document.body, {{
                attributes: true,
                attributeFilter: ['class']
            }});
        }});
    </script>
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
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.4rem 0.8rem;
            color: var(--text-color);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 400;
            background: transparent;
            border: 1px solid var(--border-color);
            border-radius: 4px;
            transition: all 0.2s ease;
        }}
        .back-link:hover {{
            color: var(--primary-color);
            border-color: var(--primary-color);
        }}
        .nav-left {{
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}
        
        .breadcrumb-section {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}
        .folder-path {{
             font-size: 0.8rem;
             color: var(--text-color-secondary);
             opacity: 0.7;
         }}
         .current-page-title {{
             font-size: 1.3rem;
             font-weight: 700;
             color: var(--text-color);
             margin: 0;
             line-height: 1.3;
             letter-spacing: -0.01em;
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
            margin: 1rem 0;
        }}
        .note-content ul {{
            list-style-type: disc;
        }}
        .note-content li {{
            margin-bottom: 0.2rem;
            display: list-item;
            list-style-position: outside;
        }}
        /* Reduce spacing for nested lists */
        .note-content li ul, .note-content li ol {{
            margin: 0.3rem 0;
            padding-left: 1.5rem;
        }}
        .note-content ul li::marker {{
            color: var(--primary-color);
            font-size: 1.2em;
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
            .navigation-header {{
                padding: 1rem;
                gap: 1rem;
                margin-bottom: 1.5rem;
            }}
            .nav-left {{
                gap: 1rem;
            }}
            .breadcrumb-section {{
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }}
            .current-page-title {{
                font-size: 1.1rem;
                text-align: left;
            }}
            .back-link {{
                font-size: 0.9rem;
                padding: 0.6rem 1rem;
                min-height: 40px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 6px;
                background: var(--border-color);
                color: var(--text-color) !important;
                text-decoration: none;
                border: 1px solid var(--border-color);
                transition: all 0.2s ease;
                flex-shrink: 0;
            }}
            .back-link:hover {{
                background: var(--primary-color);
                color: white !important;
                border-color: var(--primary-color);
            }}
            .folder-path {{
                font-size: 0.85rem;
                color: var(--text-color-secondary);
                opacity: 0.8;
                flex: 1;
                min-width: 0;
            }}
            .note-navigation {{
                width: 100%;
                display: flex;
                align-items: center;
                gap: 0.75rem;
                flex-wrap: nowrap;
            }}
            .nav-button {{
                font-size: 1.2rem;
                padding: 0.5rem;
                min-height: 40px;
                min-width: 40px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
            }}
            .nav-button span:not(.nav-icon) {{
                display: none;
            }}
            .nav-progress {{
                flex: 1;
                font-size: 0.8rem;
                text-align: center;
                color: var(--text-color-secondary);
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
        
        /* Navigation header styles */
         .navigation-header {{
             display: flex;
             flex-direction: column;
             gap: 1.25rem;
             margin-bottom: 2rem;
             padding: 1.25rem;
             background: transparent;
             border-radius: 0;
             border: none;
             border-bottom: 1px solid var(--border-color);
         }}
         
         /* Navigation buttons styles */
         .note-navigation {{
             display: flex;
             justify-content: center;
             align-items: center;
             gap: 1rem;
         }}
         
         .nav-button {{
             display: inline-flex;
             align-items: center;
             justify-content: center;
             padding: 0.6rem;
             background: transparent;
             border: 1px solid var(--border-color);
             border-radius: 4px;
             color: var(--text-color);
             text-decoration: none;
             font-size: 1rem;
             font-weight: 400;
             transition: all 0.2s ease;
             width: 36px;
             height: 36px;
         }}
         
         .nav-button:hover {{
             color: var(--primary-color);
             border-color: var(--primary-color);
         }}
         
         .nav-button:disabled {{
             opacity: 0.5;
             cursor: not-allowed;
             pointer-events: none;
         }}
         
         .nav-button.prev {{
             justify-content: flex-start;
         }}
         
         .nav-button.next {{
             justify-content: flex-end;
         }}
         
         .nav-button-text {{
             display: flex;
             flex-direction: column;
             align-items: inherit;
         }}
         
         .nav-button-label {{
             font-size: 0.75rem;
             opacity: 0.7;
             margin-bottom: 0.2rem;
         }}
         
         .nav-button-title {{
             font-weight: 500;
             max-width: 200px;
             overflow: hidden;
             text-overflow: ellipsis;
             white-space: nowrap;
         }}
         
         .nav-progress {{
             display: flex;
             flex-direction: column;
             align-items: center;
             gap: 0.5rem;
             flex: 1;
             margin: 0 1rem;
         }}
         
         .nav-progress-text {{
             font-size: 0.8rem;
             font-weight: 400;
             color: var(--text-color);
             opacity: 0.7;
             text-align: center;
         }}
         
         .nav-progress-bar {{
             width: 100%;
             max-width: 200px;
             height: 4px;
             background: #f0f0f0;
             border-radius: 2px;
             overflow: hidden;
         }}
         
         .nav-progress-fill {{
             height: 100%;
             background: #007acc;
             transition: width 0.3s ease;
         }}
         
         @media (max-width: 768px) {{
              .note-navigation {{
                  flex-direction: row;
                  gap: 0.75rem;
                  align-items: center;
              }}
              
              .nav-button {{
                  width: 40px;
                  min-width: 40px;
                  height: 40px;
                  border-radius: 50%;
                  padding: 0.5rem;
                  font-size: 1.2rem;
              }}
              
              .nav-progress {{
                  flex: 1;
                  margin: 0;
              }}
              
              .nav-button-title {{
                  max-width: none;
              }}
          }}
          
          /* Jupyter Notebook Styles */
          .code-cell {{
              margin: 1.5rem 0;
              border: 1px solid var(--border-color);
              border-radius: 8px;
              overflow: hidden;
              background: var(--bg-color);
          }}
          
          .markdown-cell {{
              margin: 1.5rem 0;
              padding: 1rem;
              background: var(--bg-color);
              border-radius: 8px;
          }}
          
          .input-area {{
              background: var(--code-bg, #f8f9fa);
              border-bottom: 1px solid var(--border-color);
          }}
          
          .input-area pre {{
              margin: 0;
              padding: 1rem;
              background: transparent;
              border-radius: 0;
              overflow-x: auto;
          }}
          
          .input-area code {{
              background: transparent;
              padding: 0;
              border-radius: 0;
              font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
              font-size: 0.9rem;
              line-height: 1.4;
          }}
          
          .output-area {{
              background: var(--bg-color);
              padding: 1rem;
          }}
          
          .output-stream {{
              background: var(--secondary-bg, #f1f3f4);
              padding: 0.75rem;
              margin: 0.5rem 0;
              border-radius: 4px;
              font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
              font-size: 0.85rem;
              line-height: 1.4;
              color: var(--text-color);
              border-left: 3px solid var(--primary-color);
          }}
          
          .output-result {{
              background: var(--bg-color);
              padding: 0.75rem;
              margin: 0.5rem 0;
              border-radius: 4px;
              font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
              font-size: 0.85rem;
              line-height: 1.4;
              color: var(--text-color);
              border: 1px solid var(--border-color);
          }}
          
          .output-image {{
              text-align: center;
              margin: 1rem 0;
              padding: 0.5rem;
              background: var(--bg-color);
              border-radius: 4px;
          }}
          
          .output-image img {{
              max-width: 100%;
              height: auto;
              border-radius: 4px;
              box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
              margin: 0;
          }}
          
          .output-html {{
              margin: 0.5rem 0;
              padding: 0.75rem;
              background: var(--bg-color);
              border-radius: 4px;
              border: 1px solid var(--border-color);
              overflow-x: auto;
          }}
          
          .output-html table {{
              width: 100%;
              border-collapse: collapse;
              margin: 0;
          }}
          
          .output-html th,
          .output-html td {{
              padding: 0.5rem;
              border: 1px solid var(--border-color);
              text-align: left;
          }}
          
          .output-html th {{
              background: var(--secondary-bg, #f8f9fa);
              font-weight: 600;
          }}
          
          .output-error {{
              background: #fef2f2;
              border: 1px solid #fecaca;
              border-radius: 4px;
              margin: 0.5rem 0;
              padding: 0.75rem;
          }}
          
          .error-name {{
              color: #dc2626;
              font-weight: 600;
              margin: 0 0 0.5rem 0;
              font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
              font-size: 0.9rem;
          }}
          
          .error-traceback {{
              color: #7f1d1d;
              margin: 0;
              font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
              font-size: 0.8rem;
              line-height: 1.4;
              background: #fef7f7;
              padding: 0.5rem;
              border-radius: 3px;
              overflow-x: auto;
          }}
          
          /* Dark theme adjustments for error outputs */
          .dark-theme .output-error {{
              background: #2d1b1b;
              border-color: #7f1d1d;
          }}
          
          .dark-theme .error-name {{
              color: #f87171;
          }}
          
          .dark-theme .error-traceback {{
              color: #fca5a5;
              background: #1f1515;
          }}
          
          /* Dark mode adjustments for Jupyter cells */
          @media (prefers-color-scheme: dark) {{
              .input-area {{
                  background: var(--code-bg, #2d3748);
              }}
              
              .output-stream {{
                  background: var(--secondary-bg, #4a5568);
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
                    <a href="mailto:alvaro.mrgr@gmail.com" aria-label="Email">
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
                <div class="navigation-header">
                    <div class="nav-left">
                        <div class="breadcrumb-section">
                            <a href="{path_prefix}notes.html" class="back-link">
                                <span>←</span>
                                <span>Back to Notes</span>
                            </a>
                            {folder_breadcrumb}
                        </div>
                        <div class="current-page-title" id="currentPageTitle"></div>
                    </div>
                    
                    <div class="note-navigation" id="noteNavigation">
                        <a href="#" class="nav-button prev" id="prevButton" style="visibility: hidden;" title="Previous note">
                            <span class="nav-icon">←</span>
                        </a>
                        
                        <div class="nav-progress">
                            <div class="nav-progress-text" id="progressText">Loading...</div>
                            <div class="nav-progress-bar">
                                <div class="nav-progress-fill" id="progressFill" style="width: 0%;"></div>
                            </div>
                        </div>
                        
                        <a href="#" class="nav-button next" id="nextButton" style="visibility: hidden;" title="Next note">
                            <span class="nav-icon">→</span>
                        </a>
                    </div>
                </div>
                
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
    
    # Add the navigation JavaScript separately to avoid f-string issues
    navigation_js = f'''
    <script>
        // Note navigation functionality
        document.addEventListener('DOMContentLoaded', function() {{
            loadNoteNavigation();
        }});
        
        async function loadNoteNavigation() {{
            try {{
                // Get current page path relative to root
                const currentPath = window.location.pathname;
                const pathParts = currentPath.split('/');
                const fileName = pathParts[pathParts.length - 1];
                
                // Construct the relative path to match navigation data
                let relativePath = '';
                if (pathParts.includes('notes')) {{
                    const notesIndex = pathParts.indexOf('notes');
                    relativePath = pathParts.slice(notesIndex).join('/');
                }} else {{
                    relativePath = 'notes/' + fileName;
                }}
                
                // Decode URL encoding (e.g., %20 -> space) to match navigation data
                relativePath = decodeURIComponent(relativePath);
                
                // Load navigation data
                const response = await fetch('{path_prefix}notes_navigation.json');
                if (!response.ok) {{
                    console.log('Navigation data not found');
                    return;
                }}
                
                const navigationData = await response.json();
                const currentNav = navigationData[relativePath];
                
                if (!currentNav) {{
                    console.log('Current page not found in navigation data:', relativePath);
                    return;
                }}
                
                // Update progress
                const progressText = document.getElementById('progressText');
                const progressFill = document.getElementById('progressFill');
                const progress = ((currentNav.current_index + 1) / currentNav.total_notes) * 100;
                
                progressText.textContent = `${{currentNav.current_index + 1}} of ${{currentNav.total_notes}}`;
                progressFill.style.width = `${{progress}}%`;
                
                // Update current page title in header
                const currentPageTitle = document.getElementById('currentPageTitle');
                const pageTitle = relativePath.split('/').pop().replace('.html', '').replace(/_/g, ' ');
                currentPageTitle.textContent = pageTitle;
                
                // Update previous button
                const prevButton = document.getElementById('prevButton');
                
                if (currentNav.previous) {{
                    prevButton.href = '{path_prefix}' + currentNav.previous;
                    prevButton.title = 'Previous: ' + currentNav.previous_title;
                    prevButton.style.visibility = 'visible';
                }} else {{
                    prevButton.style.visibility = 'hidden';
                }}
                
                // Update next button
                const nextButton = document.getElementById('nextButton');
                
                if (currentNav.next) {{
                    nextButton.href = '{path_prefix}' + currentNav.next;
                    nextButton.title = 'Next: ' + currentNav.next_title;
                    nextButton.style.visibility = 'visible';
                }} else {{
                    nextButton.style.visibility = 'hidden';
                }}
                
                // Add keyboard navigation
                document.addEventListener('keydown', function(e) {{
                    if (e.ctrlKey || e.metaKey) return; // Don't interfere with browser shortcuts
                    
                    if (e.key === 'ArrowLeft' && currentNav.previous) {{
                        window.location.href = '{path_prefix}' + currentNav.previous;
                    }} else if (e.key === 'ArrowRight' && currentNav.next) {{
                        window.location.href = '{path_prefix}' + currentNav.next;
                    }}
                }});
                
            }} catch (error) {{
                console.error('Error loading navigation:', error);
                document.getElementById('progressText').textContent = 'Navigation unavailable';
            }}
        }}
    </script>
</body>
</html>'''
    
    # Insert the navigation script before the closing body tag
    html_template = html_template.replace('</body>', navigation_js.replace('</body>', '').replace('</html>', '') + '</body>')
    
    return html_template

def process_notes_directory():
    """Process all markdown and Jupyter notebook files in the notes directory structure recursively."""
    notes_dir = Path('.')
    processed_files = 0
    failed_files = 0
    
    print("Recursively scanning notes directory for Markdown and Jupyter notebook files...")
    
    # Find all markdown and notebook files in the current directory and all subdirectories
    md_files = list(notes_dir.glob('**/*.md'))
    ipynb_files = list(notes_dir.glob('**/*.ipynb'))
    
    all_files = md_files + ipynb_files
    
    if not all_files:
        print("No Markdown or Jupyter notebook files found.")
        return

    # Process markdown files
    for md_file in md_files:
        # Skip files in directories that should be ignored
        if any(part.startswith('.') or part == '__pycache__' for part in md_file.parts):
            continue

        # Determine the depth of the file to create the correct relative path prefix.
        relative_path = md_file.relative_to(notes_dir)
        depth = len(relative_path.parent.parts)
        path_prefix = '../' * (depth + 1)
        output_dir = md_file.parent
        
        print(f"Processing Markdown: {relative_path}")
        
        if convert_md_to_html(md_file, output_dir, path_prefix, relative_path.parent):
            processed_files += 1
            print(f" -> Generated: {output_dir / f'{md_file.stem}.html'}")
        else:
            failed_files += 1
            print(f" -> Failed: {relative_path}")

    # Process Jupyter notebook files
    for ipynb_file in ipynb_files:
        # Skip files in directories that should be ignored
        if any(part.startswith('.') or part == '__pycache__' for part in ipynb_file.parts):
            continue

        # Determine the depth of the file to create the correct relative path prefix.
        relative_path = ipynb_file.relative_to(notes_dir)
        depth = len(relative_path.parent.parts)
        path_prefix = '../' * (depth + 1)
        output_dir = ipynb_file.parent
        
        print(f"Processing Jupyter Notebook: {relative_path}")
        
        if convert_ipynb_to_html(ipynb_file, output_dir, path_prefix, relative_path.parent):
            processed_files += 1
            print(f" -> Generated: {output_dir / f'{ipynb_file.stem}.html'}")
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