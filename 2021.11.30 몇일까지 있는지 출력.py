#월을 임력받아서 몇일까지 있는지 알려주는 프로그램

a=int(input('월을 임력해 주세요(1~12)'))

if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print('[',a,']달은 31일까지 있어요')
elif a==4 or a==6 or a==9 or a==11:
    print('[',a,']달은 30일까지 있어요')
elif a==2:
    print('[',a,']달은 28일까지 있어요')
else:
    print('[',a,']달은 몰라요 그게 먼데 무서워')
