#점수를 받아서 인서울 가능 여부 판단하는 프로그램

a=int(input('점수를 임력해 주세요'))

if a>100:
    print('사람이세요?')
elif a>90:
    print('A!!!1!!11')
elif a>80:
    print('B!!')
elif a>70:
    print('C')
elif a>60:
    print('D (:<<<<)')
else:
    print('인서울 실패')
