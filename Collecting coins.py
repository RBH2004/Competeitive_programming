n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    q=[]
    for j in p:
        q.append(int(j))
    a,b=q[0],q[1]
    print(int(b//2)*a)
