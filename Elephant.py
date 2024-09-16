import math
n=int(input())
counter=0
min=math.inf
my_list=[]
for i in range(5,0,-1):
    counter=(n/i)
    my_list.append(counter)
new_list=[]
for i in my_list:
    new_list.append(str(i))
final_list=[]
bounter=0
for i in new_list:
    for j in range(len(i)):
        if i[j]=="." and i[j-1]=="9":
            bounter+=1
    if bounter>=1:
        final_list.append(int(float(i)+1))
    else:
        final_list.append((float(i)))
print(final_list)
for i in final_list:
    s=int(i*10)-(int(i)*10)
    if i<min and s==0:
        min=i
print(int(min))

