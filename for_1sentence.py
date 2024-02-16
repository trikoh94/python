#출석번호가 1,2,3,4 이런식인데 > 101,102,103,,꼴로 바꾸고 싶을 때
student=[1,2,3,4,5]
print(student)
student=[i+100 for i in student]  #재정의
print(student)

#학생이름을 길이로 변환
#students= ["Tom","Gary","Anna"]
#students=[len(i) for i in students]
#print(students)

#학생이름을 대문자로 변환
students= ["Tom","Gary","Anna"]
students= [i.upper() for i in students]
print(students)