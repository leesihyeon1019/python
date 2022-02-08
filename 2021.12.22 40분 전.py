#임력받은 시간에서 40분 빼기

a,b=input().split(':')

a=int(a)
b=int(b)
c=0

if (b-40)<0:
    if a==0:
        a=23
        b=60-(b-40)*-1
    else:
        a=a-1
        b=60-(b-40)*-1
else:
    b=60-b

print(a,b,sep=':')
