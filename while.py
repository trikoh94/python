#while
customer="수연"
index=5
while index >=1:
    print("{0},커피가 준비되었다.{1}번남았다.".format(customer,index))
    index -=1
    if index==0:
        print("커피 이제 없어요")


customer= "토르"
person="unknown"
while person !=customer:
    print("{0},커피가 준비되었어요".format(customer) )
    person=input("이름이 어떻게?")
