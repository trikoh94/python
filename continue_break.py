
absent =[1,2]
no_book =[7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 끝 {0}번은 따라와".format(student))
        break
    print("{0}번은 책을 읽어라.".format(student))
