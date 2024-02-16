
try:
    print("나누기 전용 계산기 입니다.")
    nums=[]
    nums.append(int(input("첫번째 숫자:")))
    nums.append(int(input("두번째 숫자:")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0}나누기 {1}= {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)

except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

finally:  #잘 실행되어도, 에러가 난다고 해도 무조건 실행됨.
    print("계산기를 이용해주셔서 감사합니다")
