def open_account():
    print("새로운 계좌가 생성되었다.")

def deposit(balance,money): #입금
    print("입금이 완료되었습니다.잔액은{0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance,money):#출금
    if balance>=money:
        print("출금완료. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금불가. 잔액은 {0}원입니다.".format(balance))
        return balance
    
balance=0
balance=deposit(balance,1000)
balance=withdraw(balance,500)   #^^ 발란스=함수( )꼴로 만들기

def withdraw_night(balance,money):
    commission=100
    return commission,balance-money-commission

balance= 0
balance=deposit(balance,1200)
commission,balance=withdraw_night(balance,500)
print("수수료는{0}원이며 남은 잔액은{1}원이다".format(commission,balance))
