s=input()
new_string=""
my_list=[]
for i in range(len(s)):
    if s[i]==" ":
        my_list.append(int(new_string))
        new_string=""
    elif "0"<=s[i]<="9":
        new_string+=s[i]
my_list.append(int(new_string))
final_list=[]
counter=0
for i in range(len(my_list)):
    if my_list[i] not in final_list:
        final_list.append(my_list[i])

print(len(my_list)-len(final_list))
