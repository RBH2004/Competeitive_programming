n=int(input())
counter=0
sum=0
s=0
flag=True
for i in range(1,n+1,1):
    s=0
    for j in range(1,i+1,1):
        s+=j
    sum+=s
    if sum>n:
        break
    else:
        counter+=1
print(counter)

