n=int(input())
for i in range(n):
    m=int(input())
    counter=1
    i=1
    while counter<=m:
        s=str(i)
        if i%3==0 or s[len(s)-1]=="3":
            i+=1
            pass
        else:
            counter+=1
            ans=i
            i+=1
    print(ans)
