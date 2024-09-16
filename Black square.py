s=input()
p=s.split(" ")
m=input()
a,b,c,d=int(p[0]),int(p[1]),int(p[2]),int(p[3])
counter=0
for i in m:
    if i=="1":
        counter+=a
    elif i=="2":
        counter+=b
    elif i=="3":
        counter+=c
    elif i=="4":
        counter+=d
print(counter)
