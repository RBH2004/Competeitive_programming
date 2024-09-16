s=input()
my_list=[]
new_string=""
p,q,r=0,0,0
for i in range(len(s)):
    if s[i]==" ":
        my_list.append(int(new_string))
        new_string=""
    elif "0"<=s[i]<="9":
        new_string+=s[i]
my_list.append(int(new_string))
p,q,r=my_list[0],my_list[1],my_list[2]
sum=0
for i in range(1,r+1):
    sum+=p*i
if sum<=q:
    print(0)
else:
    print(sum-q)
