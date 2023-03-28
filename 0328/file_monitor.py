import os
import time
import re

DIR_WATCH = "static"

previous_files = set(os.listdir(DIR_WATCH))

while True:
    time.sleep(1)
    print("모니터링중")
    current_files = set(os.listdir(DIR_WATCH))
    new_files = current_files - previous_files
    for file in new_files:
        if file.endswith("php"):
            print(f"새로 생성된 파일 중 {file}")
            file_path = os.path.join(DIR_WATCH, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("#") or line.startswith("//"):
                        print(f"주석처리된 라인 {line}")
                    elif re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line):
                        print(f"Email address found: {line}")
    previous_files = current_files