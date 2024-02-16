#import travel.thailand  #모듈,패키지만 바로 임포트로 소환가능, 클래스,함수x
#trip_to= travel.thailand.ThailandPackage()
#trip_to.detail()

#from travel.thailand import ThailandPackage
#trip_to=ThailandPackage()
#trip_to.detail()

#import travel.vietnam
#trip_to=travel.vietnam.vietnamPackage()
#trip_to.detail()


from travel import*  #이거 쓰려면 __all__로 범위 지정해줘야함.
#trip_to=vietnam.vietnamPackage()
#trip_to.detail()

#trip_to=thailand.ThailandPackage()
#trip_to.detail()


#패키지, 모듈 위치 찾는 법

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

