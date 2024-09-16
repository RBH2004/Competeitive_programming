s=input()
my_list=[]
my_string=""
for i in s:
    if "0"<=i<="9":
        my_string+=i
    elif i=="+":
        my_list.append(int(my_string))
        my_string=""
my_list.append(int(my_string))
for i in range(len(my_list)):
    for j in range(len(my_list)-1):
        if my_list[j]>my_list[j+1]:
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
new_string=''
for i in range(len(my_list)):
    if i==len(my_list)-1:
        new_string+=str(my_list[i])
    else:
        new_string+=(str(my_list[i])+"+")
print(new_string)


