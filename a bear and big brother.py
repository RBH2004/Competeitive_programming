s=input()
n1=0
n2=0
new_string=""
counter=0
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
while (n1<=n2):
    n1*=3
    n2*=2
    counter+=1
print(counter)
