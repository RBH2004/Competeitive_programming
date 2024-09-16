n=int(input())
for j in range(n):
    p=int(input())
    ps=str(p)
    q=len(ps)
    my_list=[]
    for i in range(len(ps)):
        p=int(ps[q-1-i])*(10**i)
        if p==0:
            pass
        else:
            my_list.append(p)
    print(len(my_list))
    for k in range(len(my_list)-1,-1,-1):
        print(my_list[k],end=" ")


