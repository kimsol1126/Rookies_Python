import os

#상대경로
#dir_path = os.getcwd()
dir_path = "static"

all_files = os.listdir(dir_path)

txt_files = [] #리스트 정보를 저장하는 용
for f in all_files:
    if f.endswith('.txt'):
        txt_files.append(f)
#txt_files_lambda = [f for f in all_files if f.endswith('.txt')]

print("==== txt 파일 목록은 ====")
for f in txt_files:
    print(f)

filename = input("어떤 파일을 열람할까요?")

if filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())
else:
    print("요청한 파일이 없습니다.")