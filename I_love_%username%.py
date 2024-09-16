n=int(input())
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
max=my_list[0]
max_list=[]
min=my_list[0]
min_list=[]
for i in my_list:
    if i>max:
        max_list.append(i)
        max=i
    elif i<min:
        min_list.append(i)
        min=i
print(len(max_list)+len(min_list))

