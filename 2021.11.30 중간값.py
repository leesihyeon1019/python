#임력받은 수 3개 중 최소값을 구하는 프로그램

a=int(input('숫자 1?'))
b=int(input('숫자 2?'))
c=int(input('숫자 3?'))

if a<b and a<c:
    print('최소값은 [',a,']입니다')
elif b<a and b<c:
    print('최소값은 [',b,']입니다')
elif c<a and c<b:
    print('최소값은 [',c,']입니다')
else:
    print('최소값은 [',a,']입니다')
