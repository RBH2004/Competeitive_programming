s=(input())
new_string=""
my_list=[]
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        my_list.append(int(new_string))
        new_string=""
my_list.append(int(new_string))
n1=my_list[0]
n2=my_list[1]
n3=my_list[2]
area=n1*n2
print(n1,n2,n3)
sq_area=n3*n3
print(sq_area)
print(area)
counter=0
num=(area//sq_area)
final_num=num+1
print(final_num)
