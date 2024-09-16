import math
n=int(input())
for i in range(n):
    m=int(input())
    final_list=[]
    counter=0
    for j in range(m):
        s=input()
        my_list=s.split(" ")
        f_list=[]
        for k in my_list:
            f_list.append(int(k))
        final_list+=[f_list]
    v=1
    flag=True
    ml=[]
    mil=[]
    el=[]
    for i in final_list:
        if i[0]==1:
            ml.append(i[1])
        elif i[0]==2:
            mil.append(i[1])
        elif i[0]==3:
            el.append(i[1])
    flag=False
    max=-math.inf
    min=math.inf
    for j in ml:
        if j>max:
            max=j
    for j in mil:
        if j<min:
            min=j
    for j in el:
        if max<=j<=min:
            counter+=1
    ans=(min-max+1-counter)
    if ans<0:
        print(0)
    else:
        print(ans)


