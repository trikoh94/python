#마린: 공격 유닛, 군인, 총 쏠 수 있음.
name="마린"
hp=40
damage=5

print("{0} 유닛이 설정되었다.".format(name))
print("체력{0}, 공격력{1}\n".format(hp,damage))

#탱크 :공격 유닛

tank_name="탱크"
tank_hp=150
tank_damage=35


print("{0} 유닛이 설정되었다.".format(tank_name))
print("체력{0}, 공격력{1}\n".format(tank_hp,tank_damage))

tank2_name="탱크"
tank2_hp=150
tank2_damage=35


print("{0} 유닛이 설정되었다.".format(tank2_name))
print("체력{0}, 공격력{1}\n".format(tank2_hp,tank2_damage))


def attack(name, location, damage):
    print("{0},{1}방향으로 공격 들어옴 데미지는{2}임.".format(\
        name,location,damage))
    
attack(name,"1번",damage)
attack(tank_name,"1번",tank_damage)
attack(tank2_name,"2번",tank2_damage)


