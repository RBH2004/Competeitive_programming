import math
n=int(input())
for j in range(n):
    m=int(input())
    s=input()
    my_list=s.split(" ")
    final_list=[]
    for i in my_list:
        if i not in final_list:
            final_list.append(i)
    if len(final_list)==1:
        print("YES")
    elif len(final_list)>=3:
        print("NO")
    else:

        counter_list=[]
        for i in final_list:
            counter=0
            for j in my_list:
                if i==j:
                    counter+=1
            counter_list.append(counter)
        max=-math.inf
        min=math.inf
        for k in counter_list:
            if k>=max:
                max=k
            if k<=min:
                min=k
        if (max-min)<=1:
            print("YES")
        else:
            print("NO")

