n1,n2=0,0
s=input()
new_string=""
for i in s:
    if "0"<=i<="9":
        new_string+=i
    elif i==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
z=input()
x=[]
for k in z:
    x.append(k)

string=""
for j in range(n2):
    flag=True
    for i in range(n1-1):
        if flag==False:
            flag=True
            continue
        if x[i]=="B" and x[i+1]=="G":
            temp=x[i]
            x[i]=x[i+1]
            x[i+1]=temp
            flag=False
new_string=""
for i in x:
    new_string+=i
print(new_string)
