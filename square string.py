n=int(input())
for i in range(n):
    s=input()
    m=len(s)
    p=m//2
    c=""
    d=""
    if m==1:
        print("NO")
        continue
    else:
        c=s[:p:]
        d=s[p::]
        if c==d:
            print("YES")
        else:
            print("NO")
