n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    m,n=int(p[0]),int(p[1])
    if m<n:
        print("NO")
    elif m==n:
        print("YES")
    else:

