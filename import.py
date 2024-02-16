#glob : 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일

#os :운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder="sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제함")
else:
   os.makedirs(folder) #폴더생성
   print(folder,"폴더 생성")



 #time 시간 관련 외장함수

import time
print(time.localtime())  
print(time.strftime("%Y-%M-%d %H:%M"))

import datetime
#print(datetime.date.today())

#timedalta :두 날짜 사이의 간격
today=datetime.date.today()
td=datetime.timedelta(days=100)
print("우리가 만난지 100일 후는",today+td)
