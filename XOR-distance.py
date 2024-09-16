import math
n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    q=[]
    min=math.inf
    for k in p:
        q.append(int(k))
    a,b,r=q[0],q[1],q[2]
    def xor(m,n):
        return m^n
    if r==0:
        print(abs(xor(a,0)-xor(b,0)))
    else:
        for j in range(r):
            sum=0
            result=abs(xor(a,j)-xor(b,j))
            if result<=min:
                min=result
        print(min)

