class Unit:
    def__init__(self,name,hp,damage) :
    self.name=name
    self.hp=hp
    self.damage=damage
    print("{0}유닛이 생성되었다.".format(self.name))
    print("체력 {0},공격력{1}".format(self.hp,self.damage))


marine1= Unit("마린",40,5)
marine2= Unit("마린",40,5)
tank1=Unit("tank",34,32)
tank2=Unit("tank2",55,4)