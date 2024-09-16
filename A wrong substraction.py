s=input()
n1=0
n2=0
new_string=""
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        n1=int(new_string)
        new_string=""
n2=int(new_string)
for i in range(n2):
    f=str(n1)
    if f[len(f)-1]=="0":
        n1=n1/10
        n1=int(n1)
    elif "1"<=f[len(f)-1]<="9":
        n1=n1-1
print(int(n1))



