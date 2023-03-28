import os
import re

dir_path = "static"

all_files = os.listdir(dir_path)

txt_files = [] #리스트 정보를 저장하는 용
for f in all_files:
    if f.endswith('.php') or f.endswith('.html'):
        file_path = os.path.join(dir_path, f)
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#") or line.startswith("//"):
                    print(f"주석처리된 라인 {line}")
                #정규표현식을 사용한 이메일 주소 탐색
                elif re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line):
                    print("Email address found: " + line)

                #print(f"{file_path}를 라인 별로 출력하기 ---> {line}")
