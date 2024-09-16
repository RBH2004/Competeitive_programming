n=int(input())
for i in range(n):
    s=input()
    v=s.split(" ")
    a,b=int(v[0]),int(v[1])
    p=input()
    q=input()
    counter=0
    flag=False
    counter_list=[]
    for j in q:
        if j not in counter_list:
            counter_list.append(j)
    for j in p:
        if j not in counter_list:
            counter_list.append(j)
    if len(counter_list)==1:
        while True:
            if q not in p:
                p+=p
                counter+=1
            elif q in p:
                flag=True
                print(counter)
                break
    else:
        while True:
            if q in p:
                flag=True
                break
            else:
                p+=p
                counter+=1
            if counter>5:
                flag=False
                break
        if flag==True:
            print(counter)
        else:
            print(-1)
