
class Soldouterror(Exception):
     pass
     


chiken=10
waiting=1 #홀 안에는 현재 만석,대기번호 1번부터 시작
while(True):
        try:
          
            print("남은치킨{0}마리".format(chiken))
            order=int(input("주문 넣을 치킨은 몇 마리? "))
            if order > chiken:
                 print("치킨이 부족해요")
            elif order<=0:
                 raise ValueError    
            else:
                 print("대기번회{0}번 손님, 주문한 치킨수:{1}".format(waiting,order))
                 waiting+=1
                 chiken-=order

            if chiken==0:
                 raise Soldouterror
            
        except ValueError:
             print("잘못된 값을 입력했어요.")
        except Soldouterror:
             print("재고가 소진되어 주문 안받음")
             break



            