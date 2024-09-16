s=(input())
s1=(input())
s1_list=[]
counter=0
n1=0
n2=0
new_string=""
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
s_string=""
for i in range(len(s1)):
    if "0"<=s1[i]<="9":
        s_string+=s1[i]
    if s1[i]==" ":
        s1_list.append(int(s_string))
        s_string=""
s1_list.append(int(s_string))
for i in range(n1):
    if s1_list[i]<=n2:
        counter+=1
    else:
        counter+=2
print(counter)

