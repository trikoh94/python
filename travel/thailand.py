class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 태국 식도락 여행 55만원")
    name=str
if __name__== "__main__":
    print("Thailand 모듈을 직접실행")
    print("이 문장은 모듈을 직접실행할 때만 나옴")
    trip_to=ThailandPackage()
    trip_to.detail()
else:
    print("외부에서 호출")