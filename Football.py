s=input()
if s[len(s)-1]=="0":
    s+="1"
else:
    s+="0"
z_counter=0
o_counter=0
my_list=[]
for i in range(len(s)-1):
    if s[i]=="0":
        if s[i]=="0" and s[i+1]=="0" :
            z_counter+=1
        elif s[i]=="0" and s[i+1]!="0":
            z_counter+=1
            my_list.append(z_counter)
            z_counter=0
            continue
    elif s[i]=="1":
        if s[i]=="1" and s[i+1]=="1" :
            o_counter+=1
        elif s[i]=="1" and s[i+1]!="1":
            o_counter+=1
            my_list.append(o_counter)
            o_counter=0
            continue
flag=True
for j in my_list:
    if j>=7:
        flag=False
        break
if flag==True:
    print("NO")
else:
    print("YES")
