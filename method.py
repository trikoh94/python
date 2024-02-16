#일반유닛
#class Unit:
##    def __init__(self,name,hp):  #init 함수에 제시된 항목 self 제외하고 다 호출해야 성립함.
#       self.name=name
#        self.hp=hp
       
#공격 유닛
        
#class AttackUnit:
#    def __init__(self,name,hp,damage):
#        self.name =name
#        self.hp= hp
#        self.damage= damage


#위의 경우 일반유닛과 공격유닛이 겹치기 때문에 위의 유닛을 아래로 상속할 수 있음.
        

#일반유닛
class Unit:
    def __init__(self,name,hp):  #init 함수에 제시된 항목 self 제외하고 다 호출해야 성립함.
        self.name=name
        self.hp=hp

class AttackUnit(Unit):  #괄호 안에 Unit 위의 유닛 이름넣어주기
    def __init__(self, name, hp,damage):
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
      AttackUnit.__init__(self,name,hp,damage)
      Flyable.__init__(self,flying_speed)
      

#valkyrie= FlyableAttackUnit("발키리",200,6,5)
#valkyrie.fly(valkyrie.name,"5시")

        


