import os

# Define source folder and target HTML file
source_folder = "../_posts/csts"
target_html_path = "../docs/index.html"

# Function to generate the section list for the slides
def generate_section_list(source_folder):
    section_list = ""
    
    # Loop through files in the source folder
    for root, _, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith(".md"):
                # Generate the section for each Markdown file
                file_path = os.path.join(root, filename)
                # Extract the relative path from the source folder
                relative_path = os.path.relpath(file_path, source_folder)
                
                # Create the section tag for this file
                section_tag = f'<section data-markdown="{relative_path}" data-separator="\\n---" data-separator-vertical="\\n--"></section>\n'
                
                # Append the section tag to the section_list
                section_list += section_tag
    
    return section_list

# Generate the section list
section_list = generate_section_list(source_folder)

print(section_list)

# Read the target HTML file
with open(target_html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Find the <div class="slides"> tag and insert the section list inside it
start_tag = '<div class="slides">'
end_tag = '</div>'

start_index = html_content.find(start_tag)
end_index = html_content.find(end_tag)

if start_index != -1 and end_index != -1:
    # Replace the content inside <div class="slides"> with the section list
    html_content = html_content[:start_index + len(start_tag)] + section_list + html_content[end_index:]

# Write the updated content back to the target HTML file
with open(target_html_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"Updated {target_html_path} with the new section list inside <div class='slides'>.")