s=input()
new_string=""
n1,n2=0,0
for i in s:
    if "0"<=i<="9":
        new_string+=i
    elif i==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
print((n1*n2)//2)
