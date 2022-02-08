#두 정수의 공배수 출력하는 프로그램

a=int(input('숫자1='))
b=int(input('숫자2='))

for x in range(1,101):
    if x%a==0 and x%b==0:
        print(x)
