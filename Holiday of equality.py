n=int(input())
s=input()
a_list=s.split(" ")
b_list=[]
max=0
sum=0
for i in a_list:
    if i not in b_list:
        b_list.append(int(i))
for j in b_list:
    if j>max:
        max=j
for k in b_list:
    if k<max:
        sum+=(max-k)
    elif k==max:
        sum+=0
print(sum)

