#전부 초로 바꾸는 프로그램

a = int(input('시를 임력해 주세요'))
b = int(input('분를 임력해 주세요'))
c = int(input('초를 임력해 주세요'))

a = a*3600
b = b*60

d = a+b+c

print('총[',d,']초입니다')
