import os
from datetime import datetime, date, timedelta

dir_path = "static"
file_list = os.listdir(dir_path)

for file_name in file_list:
    file_path = os.path.join(dir_path,file_name)
    created_time = datetime.fromtimestamp(os.path.getctime(file_path))#.strftime('%y/%m/%d %H:%M:%S')
    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))#.strftime('%y/%m/%d %H:%M:%S')
    time_diff = datetime.now() - created_time
    #시간이나 날짜의 연산은 timedelta를 이용
    if time_diff >= timedelta(hours=6):
        print(f"{file_name} - 6시간 이상 경과됨")
    else:
        print(f"{file_name} - 6시간 이내 경과됨")

    #print(f"{file_path}의 생성 날짜: {created_time}, 수정 날짜: {modified_time}")

    