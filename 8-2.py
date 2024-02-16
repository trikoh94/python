#빈 자리는 빈공간으로 두고 오른쪽 정렬을 하되, 총 10자리 확보
print("{0: >10}".format(500))
#양수 일 땐 +로 표시, 음수일 떈 - 표시
print("{0: >+10}".format(500))

print("{0:_>+10}".format(500))
print("{0:_<+10}".format(500))

#3자리마다 ,를 찍어주기
print("{0:,}".format(10000000000))

#3자리마다 ,를 찍어주기 ,+.- 부호 붙여주기
print("{0:+,}".format(10000000000))

#3자리마다 ,를 찍어주기 ,+.- 부호 붙여주기,자릿수 확보(30),빈칸에 ^ 표시
print("{0:^<+30,}".format(100000000000000))

#소숫점 출력
print("{0:f}".format(7/3))
#소숫점 특정 자리까지만 표시(소수점 3번째 자리에서 반올림)
print("{0:.2f}".format(7/3))