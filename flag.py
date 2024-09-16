n1=0
n2=0
s=input()
new_string=""
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
my_list=[]
new_list=[]
for i in range(n1):
    s=input()
    for j in range(n2):
        new_list.append(s[j])


for i in range(1,len(new_list)+1,n2):
    my_list.append(new_list[i])


final_list=[]
counter=0
for k in my_list:
    for j in range(counter,n1+counter,1):
        if k==new_list[j] and (k not in final_list):
            flag=True
            counter+=1

        elif k in final_list and :
            flag=False
            break
        else:
            flag=False
            break
    final_list.append(k)
    if flag==False:
        break
if flag==True:
    print("Yes")
elif flag==False:
    print("No")





