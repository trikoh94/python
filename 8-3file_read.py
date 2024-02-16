score_file= open("score_txt","r",encoding="utf8")
print(score_file.read())
score_file.close()  #꼭 파일 닫아주는 것 까지 해야함.


#score_file=open("score_txt","r",encoding="utf8")
#print(score_file.readline(),end="")
#print(score_file.readline(),end="")   #줄별로 읽기, 한줄씩 띄어서 읽게 됨.
#print(score_file.readline(),end="")
#print(score_file.readline(),end="")
#score_file.close()


score_file=open("score_txt","r",encoding="utf8")  #파일이 몇 줄인지 모를떄
while True:
    line= score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()


score_file=open("score_txt","r",encoding="utf8")
lines=score_file.readlines()
for line in lines:
    print(line,end="")

score_file.close()

