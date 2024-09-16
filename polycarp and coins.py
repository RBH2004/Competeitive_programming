n=int(input())
for i in range(n):
    m=int(input())
    p,q=int(m//3),int(m//3)
    sum=m-(p*1)-(q*2)
    if sum==1:
        p+=1
    elif sum==2:
        q+=1
    print(p,q)
