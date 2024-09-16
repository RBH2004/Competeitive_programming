p=input()
n1,n2=0,0
new_string=""
for i in p:
    if "0"<=i<="9":
        new_string+=i
    elif i==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
counter=0
for i in range(1,n1+1,1):
    n2+=(5*i)
    if n2<=240:
        counter+=1
    else:
        pass
print(counter)

