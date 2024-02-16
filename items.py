scores={"수학":80, "국어":100,"영어":96}
for subject, score in scores.items():
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(5),sep=":")



 #은행 대기순번 표 001,002,003 ...
for num in range(1,21):
    print("대기번호:"+ str(num).zfill(3))   #zfill() 011꼴



#표준입력값
answer= input("아무값이나 입력하세요: ")  
print(type(answer))
print("입력값은"+answer+"입니다.")