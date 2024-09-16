n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    q=[]
    for i in p:
        q.append(int(i))
    a,b=q[0],q[1]
    my_list=[]
    d=a-b
    for j in range(0,(d)-1,1):
        my_list.append(a-j)

    for j in range(1,b+2,1):
        my_list.append(j)
    for k in my_list:
        print(k,end=" ")
    print()
