#원기둥의 겉넓이ㅣㅣㅣ
import math
r = int(input('반지름의 길이를 임력하세요'))
h = int(input('높히의 길이를 임력하세요'))
s=(2*math.pi*r*r)+(2*math.pi*r*h)
print("겉넓이는 {}".format(s))
