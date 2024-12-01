import os
import shutil

source_folder = "../_posts/csts"
target_base_folder = "../docs"

# # docs 폴더 및 서브디렉토리의 모든 파일 처리
# for root, _, files in os.walk(source_folder):
#     for filename in files:
#         if filename.endswith(".md"):
#             # 파일 이름에서 특정 위치의 문자열(csts) 추출
#             parts = filename.split("-")
#             if len(parts) >= 4:  # 파일 이름이 기대 형식인지 확인
#                 folder_name = parts[3]  # 예: csts

#                 # 대상 폴더 경로
#                 target_folder = os.path.join(target_base_folder, folder_name)

#                 # 대상 폴더 생성
#                 if not os.path.exists(target_folder):
#                     os.makedirs(target_folder)

#                 # 파일 경로 설정
#                 file_path = os.path.join(root, filename)
#                 new_file_path = os.path.join(target_folder, filename)

#                 # 파일 복사
#                 shutil.copy(file_path, new_file_path)
#                 print(f"Copied: {file_path} -> {new_file_path}")


# YAML front matter removal function (removes only the first YAML block)
def remove_first_yaml_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove only the first YAML front matter block
    if content.startswith('---'):
        end_of_yaml = content.find('---', 3)  # Find the second '---' (end of YAML block)
        if end_of_yaml != -1:
            content = content[end_of_yaml + 3:].strip()  # Remove the YAML part

    return content

# Process all files in the docs folder and subdirectories
for root, _, files in os.walk(source_folder):
    for filename in files:
        if filename.endswith(".md"):
            # Extract folder name from the file name
            parts = filename.split("-")
            if len(parts) >= 4:  # Ensure file name is in the expected format
                folder_name = parts[3]  # e.g., 'csts'

                # Target folder path
                target_folder = os.path.join(target_base_folder, folder_name)

                # Create target folder if it doesn't exist
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # Set file paths
                file_path = os.path.join(root, filename)
                new_file_path = os.path.join(target_folder, filename)

                # Remove first YAML block and copy file
                cleaned_content = remove_first_yaml_front_matter(file_path)

                # Write cleaned content to the new file
                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(cleaned_content)

                print(f"Copied: {file_path} -> {new_file_path}")
