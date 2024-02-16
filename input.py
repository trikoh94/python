language=input("어떤 언어를 좋아하나요?: ")
print("{0}언어가 좋아요".format(language))

#dir : 어떤 객체를  넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표현

print(dir())

import random
print(dir())

import pickle
print(dir())

print(dir(random))
lst=[1,2,3]
print(dir(lst))


name="Kim"
print(dir(name))