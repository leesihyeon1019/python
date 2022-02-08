#1부터 임력한 수까지 홀수 구하기

s=int(input())
x=0

while True:
    if x==s:
        break
    x+=1
    if x%2==0:
        continue
    print(x)
    
