n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    a,b=int(p[0]),int(p[1])
    if a==0:
        print(1)
    elif b==0:
        print(a+1)
    else:
        print((a*1)+(b*2)+1)

