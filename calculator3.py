

while True:

    print("what do you want to do? plz enter the number 1.plus, 2.minus 3.multiple, 4.divide 5.finish: ")

    a=input()

    if a=="5":
        break

    fn=int(input("first number: "))
    sn=int(input("second number: "))


    if a=="1":
        print("{}+{}={}".format(fn,sn,fn+sn))
    elif a=="2":
        print("{}-{}={}".format(fn,sn,fn-sn))
    elif a=="3":
        print("{}*{}={}".format(fn,sn,fn*sn))
    elif a=="4":
        print("{}/{}={}".format(fn,sn,fn/sn))