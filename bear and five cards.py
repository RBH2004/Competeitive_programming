s=input()
new_string=""
n1,n2,n3,n4,n5=0,0,0,0,0
my_list=[]
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        my_list.append(int(new_string))
        new_string=""
my_list.append(int(new_string))
n1,n2,n3,n4,n5=my_list[0],my_list[1],my_list[2],my_list[3],my_list[4]
all=n1+n2+n3+n4+n5
min=0
new_list=[]
double_index=[]
n1_c,n2_c,n3_c,n4_c,n5_c=0,0,0,0,0
for i in my_list:
    if n1==i:
        n1_c+=1
    elif n2==i:
        n2_c+=1
    elif n3==i:
        n3_c+=1
    elif n4==i:
        n4_c+=1
    elif n5==i:
        n5_c+=1
if (n1_c>1 or n2_c>1 or n3_c>1 or n4_c>1 or n5_c>1) and (n1_c or n2_c or n3_c or n5_c or n4_c)<4:
    if n1_c>1:
        temp=all
        min=all-n1*n1_c
        if min<temp:
            least=min
    if n2_c>1:
        temp=min
        min=all-n2*n2_c
        if min<temp:
            least=min
    if n3_c>1:
        temp=min
        min=all-n3*n3_c
        if min<temp:
            least=min
    if n4_c>1:
        temp=min
        min=all-n4*n4_c
        if min<temp:
            least=min
    if n5_c>1:
        temp=min
        min=all-n5*n5_c
        if min<temp:
            least=min
    print(least)
elif (n1_c or n2_c or n3_c or n4_c or n5_c)>=4:
    if n1_c>=4:
        temp=all
        min=all-n1*3
        if min<temp:
            least=min
    if n2_c>=4:
        temp=min
        min=all-n2*3
        if min<temp:
            least=min
    if n3_c>=4:
        temp=min
        min=all-n3*3
        if min<temp:
            least=min
    if n4_c>=4:
        temp=min
        min=all-n4*3
        if min<temp:
            least=min
    if n5_c>=4:
        temp=min
        min=all-n5*3
        if min<temp:
            least=min

    print(least)

else:
    print(all)
