n=int(input())
new_string=""
my_list=[]
for i in range(n):
    s=input()
    my_list.append(s)
p=len(my_list[0])
counter=0
flag=True
for i in range(p):
    for j in range(1,len(my_list)):
        if my_list[j][i]==my_list[j-1][i]:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        new_string+=my_list[j][i]
    if flag==False:
        break
print(len(new_string))
