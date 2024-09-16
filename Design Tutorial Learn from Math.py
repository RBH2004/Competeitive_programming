n=int(input())
i=0
j=0
for i in range(4,n+1):
    j=n-i
    if (i%2==0 or i%3==0 or i%4==0 or i%6==0) and (j%2==0 or j%3==0 or j%4==0 or j%5==0 or j%6==0):
        print(i,j)
        break

