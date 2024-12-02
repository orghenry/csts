import os
import shutil

source_folder = "../_posts/csts"
target_base_folder = "../docs/csts"

# Process subdirectories only (exclude files in source_folder root)
for root, dirs, files in os.walk(source_folder):
    # Calculate the relative path from source_folder
    relative_path = os.path.relpath(root, source_folder)
    
    # Skip processing the source folder itself
    if relative_path == ".":
        continue

    # Create the corresponding target directory
    target_folder = os.path.join(target_base_folder, relative_path)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Created directory: {target_folder}")

    # Copy files from the subdirectory
    for filename in files:
        file_path = os.path.join(root, filename)
        new_file_path = os.path.join(target_folder, filename)

        shutil.copy2(file_path, new_file_path)
        print(f"Copied: {file_path} -> {new_file_path}")
