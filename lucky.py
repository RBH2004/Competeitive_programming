m=int(input())
for j in range(m):
    s=input()
    sum1=0
    sum2=0
    n=len(s)
    for i in range(n//2):
        sum1+=int(s[i])
        sum2+=int(s[n-i-1])
    if sum1==sum2:
        print("YES")
    else:
        print("NO")
