#집합 set
#증복안됨, 순서 없음

my_set= {1,2,3,3,3}
print(my_set)

java ={ "유","박","김"}
python={"김","유","양"}

#교집합 (java 와 python)
print (java & python)
print (java.intersection(python))

#합집합 (java 나 python)
print (java | python)
print(java.union(python))
       

#차집합 ( java 0, python x)
print(java-python)
print(java.difference(python))

#pyhton 할줄하는 사람 추가
python.add("김태호")
print(python)

#java에서 제외
java.remove("김")
print(java)

#자료구조의 변경

menu={"커피","빵","쥬스"}
print(menu,type(menu))

menu=list(menu)
print(menu,type(menu))

menu=tuple(menu)
print(menu,type(menu))