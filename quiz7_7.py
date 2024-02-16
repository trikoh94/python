



def std_weight(height,gender):
    if gender=="male":
        return height*height*22
        print("키{0}cm 의 남자의 표준 체중은 {1}이다".format(std_weight))






def std_weight(height,gender):
    if gender=="male":
        return height*height*22
    else:
        return height*height*21
    
gender="male"    ##함수 호출 부분이 중요하다.. 
height=175
weight=round(std_weight(height/100,gender),2)
print("키{0}인 {1}사람의 표즌 체중은 {2}이다.".format(height,gender,weight))
    
