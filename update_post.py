from bs4 import BeautifulSoup

def update_blog(name, date, summary, file_path="blogs.html"):
    post_html = f'''        <article class="blog-preview">
            <h2><a href="blog/{name}/index.html">{name}</a></h2> 
            <div class="post-meta">{date}</div>
            <p>{summary}</p>
        </article>\n'''

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_marker = '<div class="content">'
    insert_pos = content.find(insert_marker)
    if insert_pos == -1:
        raise ValueError("Could not find <div class=\"content\"> in the HTML file.")

    insert_pos += len(insert_marker)
    updated_content = content[:insert_pos] + "\n" + post_html + content[insert_pos:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Blog '{name}' added successfully.")


import os
import shutil

def add_blog_post(name, iframe, template_path="blog/template.html"):
    # Define target folder and file paths
    target_folder = os.path.join("blog", name)
    target_file = os.path.join(target_folder, "index.html")

    # Create the folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Read the template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Insert iframe into the template, replacing a placeholder
    # You can also just append or prepend if needed
    if "your_iframe_here" in template:
        new_content = template.replace("your_iframe_here", iframe)
    else:
        # Fallback: just append it before </body>
        if "</body>" in template:
            new_content = template.replace("</body>", iframe + "\n</body>")
        else:
            new_content = template + "\n" + iframe

    # Write the new file
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Blog post created at {target_file}")



if __name__ == '__main__':

    
    name = str(input('What is the name of your new post?: '))
    iframe = str(input('Paste your Linkedin iFrame here: '))
    date = str(input('Add the date of the post here ("month" day, year):  '))
    summary = str(input('Write a short summary about the article: '))
    update_blog(name, date, summary)
    add_blog_post(name, iframe)

