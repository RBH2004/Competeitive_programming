m=int(input())
s=input()
flag=True
for i in s:
    if i=="1":
        flag=False
        break
    else:
        flag=True
if flag==True:
    print("EASY")
else:
    print("HARD")
