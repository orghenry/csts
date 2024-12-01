import os
import subprocess

#subprocess.run(['python', 'make_tags.py'])
#subprocess.run(['python', 'copy_docs_to_posts.py'])
subprocess.run(['python', 'copy_posts_to_docs.py'])
#subprocess.run(['python', 'make_posts_to_section_html.py'])
subprocess.run(['python', 'make_tags_url.py'])
#subprocess.run(['python', 'make_category.py'])
subprocess.run(['python', 'make_categories_url.py'])

print("All have been run.")
