n=int(input())
s=input()
my_list=[]
new_string=""
for i in s:
    if "0"<=i<="9":
        new_string+=i
    elif i==" ":
        my_list.append(int(new_string))
        new_string=""
my_list.append(int(new_string))
sum=0
for i in my_list:
    sum+=i
print(sum/n)
