import zipfile
import os

directory = "static" #static 이라는 폴더 사용
#비어있는 압축파일 하나 생성
zip_file = zipfile.ZipFile('static_folder.zip', 'w')
for root, dirs, files in os.walk(directory):
    for file in files:
        zip_file.write(os.path.join(root, file)) #경로지정
#안에 폴더가 있어도 알아서 다 압축해줌
zip_file.close()