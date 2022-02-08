#부채꼴의 넓이
import math
r = int(input('반지름'))
c = int(input('중심각'))
s= math.pi*r*r*c/360
print('부채꼴의 넓이는 {}'.format(s))
