n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    q=[]
    for i in p:
        q.append(int(i))
    a,b,c=q[0],q[1],q[2]
    if c%2!=0:
        d=(c//2)+1
        e=c-d
    elif c%2==0:
        d=c//2
        e=c-d
    if (a+d)>(b+e):
        print("First")
    else:
        print("Second")
