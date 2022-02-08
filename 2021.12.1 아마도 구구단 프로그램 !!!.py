#아마도 구구단 프로그램

n = int(input('구구단 수를 임력해 주세요'))
c = int(input('외우기 시작'))
a = int(input('외우기 끝'))
a=a+1
b=0

for x in range(c,a):
    print(n,'X',x,'= [',n*x,']')
    b=b+n*x

print('총합 [',b,']')
input('ENTER=종료')
