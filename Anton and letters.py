s=input()
my_list=[]
final_list=[]
new_string=""
for i in s:
    if "a"<=i<="z":
        new_string+=i
    elif i==",":
        my_list.append(new_string)
        new_string=""
my_list.append(new_string)
for i in my_list:
    if i=="":
        pass
    elif i not in final_list:
        final_list.append(i)

print(len(final_list))
