n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    n,a,b=int(p[0]),int(p[1]),int(p[2])
    sum1=n*a
    extra=n-2
    extra_price=extra*a
    sum2=b+extra_price
    if n==1:
        print(a)
    else:
        if sum1<=sum2:
            print(sum1)
        else:
            print(sum2)
