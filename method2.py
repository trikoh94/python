
#일반유닛
class Unit:
    def __init__(self,name,hp,damage):  #init 함수에 제시된 항목 self 제외하고 다 호출해야 성립함.
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0}유닛이 생성되었다".format(self.name))
        print("체력:{0}, 공격력:{1}".format(self.hp,self.damage))


#공격 유닛
        
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name =name
        self.hp= hp
        self.damage= damage
    
    def attack(self,location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력{2}]"\
              .format(self.name,location,self.damage))
    
    def damaged(self, damage):
        print("{0}:적군으로 부터 공격을 받아 {1}데미지를 입었다."\
              .format(self.name,damage))
        self.hp -=damage
        print("{0}: 현재 남은 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("game over")


#파이어뱃 :공격유닛
            
firebat= AttackUnit("파이어뱃",22,5)
firebat.attack("5시")

firebat.damaged(8)
firebat.damaged(13)

