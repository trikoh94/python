from random import*

#일반유닛
class Unit:
    def __init__(self,name,hp,speed):  #init 함수에 제시된 항목 self 제외하고 다 호출해야 성립함.
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0}유닛이 생성되었습니다.".format(name))
    
    def move(self,location):
        print("[지상유닛이동]")
        print("{0}:{1}방향으로 이동.[속도{2}]"\
              .format(self.name,location,self.speed))
        
    def damaged(self,damage):
        print("{0}:적군으로 부터 공격을 받아 {1}데미지를 입었다."\
              .format(self.name,damage))
        self.hp -=damage
        print("{0}: 현재 남은 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("game over")

#공격유닛
class AttackUnit(Unit):  # 
    def __init__(self, name, hp,speed,damage):
       Unit.__init__ (self,name,hp)  #상속 문장. Unit.__init__(self, ,)
       self.damage=damage #상속에 없는 것 등록해주기


    def attack(self,location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력{2}]"\
              .format(self.name,location,self.damage))

#마린    
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    
    #스팀팩: 일정 시간 동안 이동 속도 및 공격 속도 증가,체력 10 감소
    def stimpack(self):
        if self.hp > 20:
            self.hp-=10
            print("{0}:스팀팩을 사용합니다. [체력 10 감소]".format(self.name))
        else:
            print("{0}:체력이 부족하여 스팀팩 사용 불가".format(self.name))

#탱크
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)

    #시즈모드 :탱크를 지상에 고정시켜 더 높은 파워로 공격 가능, 이동 불가.
    def set_seize_mode(self):
        if Tank.seize_developed ==False:
            return
        
        #현재 시즈모드x > 시즈모드 가동      > 외부에서 시즈모드를 호출할 때 like this.
        if self.seize_mode == False:
            print("{0}: 시즈모드로 전환".format(self.name))
            self.damage*=2
            self.seize_mode =True

        else:
            print("{0}:시즈모드 중지".format(self.name))
            self.damage/=2
            self.seize_mode=False



        


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

#레이스 
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit("레이스",80,20,50)
        self.clocked= False #클로킹 모드 (해제 상태)
    
    #클로킹 능력 관련
    def clocking(self):
        if self.clocked ==True:  # 클로킹 설정 > 모드 해제
            print("{0}: 클로킹 모드를 해제한다".format(self.name))
            self.clocked=False
        if self.clocked ==False: #클로킹 해제 >설정
            print("{0}: 클로킹 모드를 설정한다".format(self.name))
            self.clocked=True


def game_start():
    print("[알림: 새로운 게임이 시작합니다.]")

def game_over():
    print("게임 gg ")
    print("[player 님이 퇴장했습니다.]")


#게임 시작
    
game_start()

#마린 3기 생성
m1=Marine()
m2=Marine()
m3=Marine()

#탱크 2기 생성
t1=Tank()
t2=Tank()

#레이스 1기 생성
w1=Wraith()

#유닛 일괄 관리(생성된 모든 유닛 append 처리)
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 가동
Tank.seize_developed=True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다")

#공격 모드 준비(마린:스팀팩, 탱크:시즈모드, 레이스:클로킹) 

for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()
    

#전군 공격
for unit in attack_units:
    unit.move("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 5~20


game_over()



