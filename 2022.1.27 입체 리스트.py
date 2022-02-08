#list를 입체적으로 보여주는 프로그램


list1=[]
list2=[]
v=1
for i in range(10):
    for k in range(10):
        list1.append(v)
        v+=1
    list2.append(list1)
    list1=[]

for i in range(10):
    for k in range(10):
        print('%3d'%list2[i][k],end=' ')
    print(' ')
