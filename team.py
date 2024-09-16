n=int(input())
counter=0
for i in range(n):
    s=input()
    sum=0
    new_string=""
    for i in range(len(s)):
        if "0"<=s[i]<="1":
            new_string+=s[i]
        elif s[i]==" ":
            sum+=int(new_string)
            new_string=""
    sum+=int(new_string)
    if sum>=2:
        counter+=1
    else:
        pass
print(counter)
