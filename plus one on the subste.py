import math
n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    my_list=s.split(" ")
    max=-math.inf
    min=math.inf
    f_list=[]
    for j in my_list:
        f_list.append(int(j))
    for k in f_list:
        if k>max:
            max=k
        if k<min:
            min=k
    print(max-min)
