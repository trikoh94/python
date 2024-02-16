class Unit:
    def __init__(self,name,hp,damage):  #init 함수에 제시된 항목 self 제외하고 다 호출해야 성립함.
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0}유닛이 생성되었다".format(self.name))
        print("체력:{0}, 공격력:{1}".format(self.hp,self.damage))

#marine1=Unit("마린",40,20)
#marine2=Unit("마린1",45,15)
#tank1=Unit("탱크",35,5)
        
wraith=Unit("레이스",90,20)
print("유닛이름: {0},유닛 공격력{1}".format(wraith.name,wraith.damage))

wraith2=Unit("빼앗는 레이스",90,20)
wraith2.clocking=True   ##clocking 이라는 변수를 추가해 줌!! 레이스2에만 성립됨.

if wraith2.clocking==True:
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))