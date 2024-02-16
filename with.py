import pickle
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))  #이전에 저장한 변수 파일을 불러올 수 있음.    