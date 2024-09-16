n=int(input())
sum=0
high=0
for j in range(n):
    n1,n2=0,0
    s=input()
    new_string=""
    for i in s:
        if "0"<=i<="9":
            new_string+=i
        elif i==" ":
            n1=int(new_string)
            new_string=""
    n2=int(new_string)
    sum-=n1
    sum+=n2
    if sum>high:
        high=sum
    else:
        pass
print(high)
