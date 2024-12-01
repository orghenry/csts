import os
import shutil

source_folder = "../_posts/csts"
target_base_folder = "../docs"

# docs 폴더 및 서브디렉토리의 모든 파일 처리
for root, _, files in os.walk(source_folder):
    for filename in files:
        if filename.endswith(".md"):
            # 파일 이름에서 특정 위치의 문자열(csts) 추출
            parts = filename.split("-")
            if len(parts) >= 4:  # 파일 이름이 기대 형식인지 확인
                folder_name = parts[3]  # 예: csts

                # 대상 폴더 경로
                target_folder = os.path.join(target_base_folder, folder_name)

                # 대상 폴더 생성
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # 파일 경로 설정
                file_path = os.path.join(root, filename)
                new_file_path = os.path.join(target_folder, filename)

                # 파일 복사
                shutil.copy(file_path, new_file_path)
                print(f"Copied: {file_path} -> {new_file_path}")