import math
p=int(input())
for i in range(p):
    q=int(input())
    r=input()
    my_list=[]
    new_string=""
    sum=0
    for j in range(len(r)):
        if "0"<=r[j]<="9":
            new_string+=r[j]
        elif r[j]==" ":
            my_list.append(int(new_string))
            new_string=""
    my_list.append(int(new_string))
    for k in my_list:
        sum+=k
    n=math.sqrt(sum)
    s=str(n)
    if s[len(s)-2]=="." and s[len(s)-1]=="0":
        print("YES")
    else:
        print("NO")

