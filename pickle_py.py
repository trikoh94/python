import pickle
profile_file= open("profile.pickle","wb")
profile={"이름":"박지성","나이":23,"취미":["농구","야구","축구"]}
print(profile)
pickle.dump(profile,profile_file)  #profile을 profile_file 안에 넣음
profile_file.close()

profile_file=open("profile.pickle","rb")
profile= pickle.load(profile_file)  #file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
