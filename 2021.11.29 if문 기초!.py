#if문 기초

a=6
b=5

if a>b:
    print('a가 터 큼')
elif a==b:
    print('둘다 같음')
else:
    print('b가 더 큼')

print(a!=b) #a와 b가 다르면 True
print(a>=b)#a가 b보다 크거나 같으면True


if a==6 and b==5:
    print('선생님 바봉')
#전부 조건이 맞으면 아래 명령을 실행

if a==6 or b==550:
    print('선생님은 역시나 바봉')
#하나만 조건이 맞으면 아래 명령을 실행
