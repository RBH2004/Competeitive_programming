s=input()
fs=s.split(" ")
ms=[]
for i in fs:
    ms.append(int(i))

p,q,r=ms[0],ms[1],ms[2]
max=0
min=100000000000000000000000000000000000
for i in ms:
    if (i)>max:
        max=i
    if (i)<min:
        min=i
print(max-min)
