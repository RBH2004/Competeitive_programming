n=int(input())
s=str(n)
flag=True
counter=0
f_counter=0
s_counter=0
for i in s:
    if i=="4":
        f_counter+=1
    if i=="7":
        s_counter+=1
sum=f_counter+s_counter
if sum==4 or sum==7:
    print("YES")
else:
    print("NO")
