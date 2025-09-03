import os
import cssutils
import logging
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
CSS_FILE_PATH = 'styles.css'
CLEANED_CSS_FILE_PATH = 'styles.cleaned.css'
SEARCH_DIRECTORY = '.'
# ---------------------

def find_all_html_files(root_dir):
    """Recursively finds all HTML files in a given directory."""
    html_files = []
    print(f"[*] Searching for HTML files in '{os.path.abspath(root_dir)}'...")
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def extract_selectors_from_html(html_files):
    """Parses HTML files and extracts all used tag names, IDs, and class names."""
    used_selectors = set()
    print(f"[*] Parsing {len(html_files)} HTML file(s) to find used selectors...")
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            # Add all tag names
            for tag in soup.find_all(True):
                used_selectors.add(tag.name)
                # Add all IDs
                if tag.has_attr('id'):
                    used_selectors.add(f'#{tag["id"]}')
                # Add all classes
                if tag.has_attr('class'):
                    for css_class in tag['class']:
                        used_selectors.add(f'.{css_class}')
    print(f"[*] Found {len(used_selectors)} unique selectors in use.")
    return used_selectors

def clean_css_file(css_path, used_selectors):
    """
    Reads a CSS file, removes unused rules, and merges duplicates.
    Returns the cleaned CSS text and statistics.
    """
    if not os.path.exists(css_path):
        print(f"[!] Error: CSS file not found at '{css_path}'")
        return None, {}

    print(f"[*] Cleaning '{css_path}'...")
    
    # Suppress cssutils's own logging to keep our output clean
    cssutils.log.setLevel(logging.CRITICAL)
    
    # cssutils automatically merges duplicate selectors upon parsing
    parser = cssutils.CSSParser()
    stylesheet = parser.parseFile(css_path, encoding='utf-8')
    
    initial_selector_count = 0
    final_selector_count = 0
    
    rules_to_remove = []

    for rule in stylesheet:
        # We only process style rules, keeping @media, @keyframes etc.
        if rule.type == rule.STYLE_RULE:
            initial_selector_count += 1
            
            # Split comma-separated selectors like 'h1, .title'
            selectors = [s.strip() for s in rule.selectorText.split(',')]
            
            # Keep track of the selectors that are actually used
            valid_selectors = []
            
            for selector in selectors:
                # Basic check: clean pseudo-classes/elements for matching
                # e.g., turn 'a:hover' into 'a' for the check
                core_selector = selector.split(':')[0].split('::')[0].split('[')[0]

                # This is a conservative approach. We keep:
                # - The universal selector '*'
                # - Anything that is not a simple tag, class, or id (e.g., attribute selectors)
                # - Selectors that are found in the HTML files
                is_complex = not (core_selector.startswith('.') or core_selector.startswith('#') or core_selector.isalnum())
                
                if selector == '*' or is_complex or core_selector in used_selectors:
                    valid_selectors.append(selector)

            if valid_selectors:
                # If some selectors are valid, update the rule
                rule.selectorText = ', '.join(valid_selectors)
                final_selector_count += 1
            else:
                # If no selectors are valid, mark the entire rule for removal
                rules_to_remove.append(rule)

    # Remove the marked rules from the stylesheet's rule list
    for rule in rules_to_remove:
        stylesheet.cssRules.remove(rule)

    stats = {
        'initial': initial_selector_count,
        'final': final_selector_count,
    }
    
    return stylesheet.cssText.decode('utf-8'), stats

def main():
    """Main function to run the CSS cleanup process."""
    html_files = find_all_html_files(SEARCH_DIRECTORY)
    if not html_files:
        print("[!] No HTML files found. Cannot determine used selectors. Aborting.")
        return

    used_selectors = extract_selectors_from_html(html_files)
    
    cleaned_css, stats = clean_css_file(CSS_FILE_PATH, used_selectors)

    if cleaned_css is None:
        return

    with open(CLEANED_CSS_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(cleaned_css)
        
    print(f"\n[+] Cleanup complete. Cleaned file saved as '{CLEANED_CSS_FILE_PATH}'")
    
    # --- Summary ---
    processed = stats['initial']
    removed = stats['initial'] - stats['final']
    reduction = (removed / processed * 100) if processed > 0 else 0
    
    print("-" * 40)
    print(f"Processed: {processed} selectors (duplicates were merged automatically).")
    print(f"Removed: {removed} unused selectors.")
    print(f"Reduction: {reduction:.2f}%")
    print("-" * 40)


if __name__ == '__main__':
    main()