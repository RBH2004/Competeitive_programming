import math
n=int(input())
s=input()
p=s.split(" ")
q=[]
f="1375"
for k in p:
    q.append(int(k))
for i in q:
    if i==1:
        print("NO")
        continue
    m=math.sqrt(i)
    s=str(math.sqrt(i))
    if s[-1]=="0" and s[-2]=="." and (i<=10 or i%2!=0):
        print("YES")
    else:
        print("NO")

