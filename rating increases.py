n=int(input())
for i in range(n):
    s=input()
    m=len(s)//2
    o=""
    t=""
    p=len(s)//2
    if len(s)%2==0:
        for j in range(m):
            o+=s[j]
            t+=s[m+j]
    elif len(s)%2!=0:
        o=s[:p:]
        t=s[p::]
    a=int(o)
    b=int(t)
    new_string=""
    while True:
        if t[0]=="0" and len(s)==3:
            print(-1)
            break
        elif b==0 and len(s)>2:
            new_string+=o[p-1]
            new_string+=t
            b=int(new_string)
            a=int(o[:p-1:])
        else:
            if b==0 or a==0:
                print(-1)
                break
            elif len(s)==2:
                if b>a:
                    print(a,b)
                    break
                else:
                    print(-1)
                    break
            elif b>a:
                print(a,b)
                break
            elif a==b:
                print(-1)
                break
            else:
                l=a%10
                a=a//10
                b=(l*(10**len(t)))+b

