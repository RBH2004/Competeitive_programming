n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    a,b=int(p[0]),int(p[1])
    if b%2==0:
        print("YES")
    else:
        print("NO")
