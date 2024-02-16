class Unit:
    def __init__(self):
        print("유닛 생성자")

class Flyable:
    def __init__(self):
        print("플라이어블 생성자")

class FlyableUnit(Flyable,Unit):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropshit=FlyableUnit()