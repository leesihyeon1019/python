#돈을 구분해주는 프로그램


#IF문 겁나 많아 살려줘

r=int(input('돈을 임력해주세요'))

a = r//1000
b = r-a*1000
c = b//100

if b >= 500:
    print('1000원[',a,']개,500원[ 1 ]개 100원[',c-5,']개')
else:
    print('1000원[',a,']개,500원[ 0 ]개 100원[',c,']개')
