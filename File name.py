n=int(input())
s=input()
counter=0
flag=True
for i in range(n-1):
    if s[i]=="x" and s[i+1]=="x":
        counter+=1
    elif s[i]!="x":
        counter=0
        continue

if counter>=2:
    extra_x=(counter+1)-2
    print(extra_x)
else:
    print("0")

