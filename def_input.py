def profile(name,age,main_lang):
    print("이름:{0}\t나이:{1}\t언어:{2}"\
          .format(name,age,main_lang))

profile("유재석",20,"python")


def profile(name,age=17,main_lang="python"):
    print("이름:{0}\t나이:{1}\t 언어:{2}"\
        .format(name,age,main_lang))
    
profile("유재석")
profile("방시혁")