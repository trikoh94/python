#score_file=open("score_txt","w",encoding="utf8")
#print("수학:0",file=score_file)
#print("영어:100",file=score_file)
#score_file.close()

score_file=open("score_txt","a",encoding="utf8")
score_file.write("과학:80")
score_file.write("\n코딩:100")
score_file.close()