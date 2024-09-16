n=int(input())
my_list=[]
for i in range(n):
    s=input()
    my_list.append(s)
counter=0
for j in range(len(my_list)-1):
    if my_list[j]==my_list[j+1]:
        pass
    else:
        counter+=1
print(counter+1)
