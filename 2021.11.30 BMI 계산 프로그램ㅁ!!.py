#키,몸무게를 임력받아 BMI를 계산하는 프로그램

a=int(input('키(CM)'))
b=int(input('몸무게(KG)'))
a=a/100
a=a**2
a=b/a

if a<20:
    print("저체중입니다")
elif a>=20 and a<24:
    print('정상입니다')
elif a>=25 and a<29:
    print('과체중입니다')
elif a>=30:
    print('비만입니다')
else:
    print('ERR404:[RTX2090.exe]를 찾을 수 없습니다')
