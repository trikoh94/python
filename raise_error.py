try:
    print("한 자리 숫자 전용 나눗셈 계산기 입니다.")
    num1=int(input("첫 번째 숫자 입력:"))
    num2=int(input("두 번째 숫자 입력:"))
    if num1 >=10 or num2>=10:
        raise ValueError
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력. 한 자리 숫자만 입력하시오.")