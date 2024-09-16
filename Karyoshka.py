n=int(input())
for i in range(n):
    s=input()
    my_list=[]
    my_list=s.split(" ")
    p,q,r=int(my_list[0]),int(my_list[1]),int(my_list[2])
    sum=0
    if (p<=q and p<=r):
        sum=p
    elif (p>=q and p>=r):
        sum=q
        sum+=int((p//2))
    print(f"Case {i+1}: {sum}")



