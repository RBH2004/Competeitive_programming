s=input()
x=input()
new_string=""
my_string=""
n1,n2=0,0
for i in s:
    if "0"<=i<="9":
        new_string+=i
    elif i==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
my_list=[]
for i in x:
    if "0"<=i<="9":
        my_string+=i
    elif i==" ":
        my_list.append(int(my_string))
        my_string=""
my_list.append(int(my_string))
counter=0
for i in my_list:
    if i>=my_list[n2-1] and i!=0:
        counter+=1
    else:
        pass
print(counter)
