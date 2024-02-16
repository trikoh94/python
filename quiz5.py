from random import *
cnt=0 #총 탑승승객 수
for i in range(1,51): #승객 수 1~50명
    time= randrange(5,51) #탑승 시간 5분~50분 소요
    if 5<= time <=15:
        print ("[0] {0}번째 탑승객 (소요시간 {1}분)".format(i,time))
        cnt+=1   # 이런 디테일 잘 추가하기
    else:
        print("[ ]{0}번째 탑승객 (소요시간 {1}분)".format(i,time))

print("총 승객수 {0}명".format(cnt))

