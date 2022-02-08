#원기둥의 부피
import math

r = int(input('반지름을 임력하세요'))
h = int(input('높이를 임력하세요'))
s=math.pi*r*r*h

print('부피는 {}'.format(s))
