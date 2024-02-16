
        

#일반유닛
class Unit:
    def __init__(self,name,hp,speed):  #init 함수에 제시된 항목 self 제외하고 다 호출해야 성립함.
        self.name=name
        self.hp=hp
        self.speed=speed
    
    def move(self,location):
        print("[지상유닛이동]")
        print("{0}:{1}방향으로 이동.[속도{2}]"\
              .format(self.name,location,self.speed))

class AttackUnit(Unit):  # 
    def __init__(self, name, hp,speed,damage):
       Unit.__init__ (self,name,hp)  #상속 문장. Unit.__init__(self, ,)
       self.damage=damage #상속에 없는 것 등록해주기


    def attack(self,location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력{2}]"\
              .format(self.name,location,self.damage))
    
    def damaged(self,damage):
        print("{0}:적군으로 부터 공격을 받아 {1}데미지를 입었다."\
              .format(self.name,damage))
        self.hp -=damage
        print("{0}: 현재 남은 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("game over")


#드랍쉽 : 공중유닛, 수송기,마린,파이어뱃,탱크 등을 수송함. 공격 x
    
#날 수 있는 유닛 생성
            

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0}:{1}번 방향으로 날아간다. 속도{2}"\
              .format(name,location,self.flying_speed))
        

#공중공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):   #다중상속 유닛 2개를 다 상속받음
    def __init__(self, name, hp, damage,flying_speed):
      AttackUnit.__init__(self,name,hp,0,damage)  #지상스피드는 0 처리
      Flyable.__init__(self,flying_speed)
      

     ## 이 부분 주목 메소드 overriding 추가해준 부분입니다.  
    def move(self,location):  
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

#벌쳐: 지상 유닛, 기동성 good

vulrture=AttackUnit("벌쳐",80,10,20)


#배틀크루져: 공중 유닛, 공격력 굳
battlecruiser= FlyableAttackUnit("배틀크루져",500,20,3)



#이렇게 공중,지상 유닛 따로 나눠서 move 함수 인지 fly 함수인지 구분하여 호출하는 게 귀찮기 때문에 method overriding이 필요함.
vulrture.move("12시")
#battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")