n=int(input())
for i in range(n):
    m=int(input())
    sum=0
    for i in range(1,m+1,1):
        if len(str(i))>1:
            p=str(i)
            for i in p:
                sum+=int(i)
        else:
            sum+=i
    print(sum)
