s=input()
my_list=s.split(" ")
final_list=[]
for i in my_list:
    final_list.append(int(i))
a,b=final_list[0],final_list[1]
d=min(a,b)
e=abs(b-a)
c=e//2
print(d,c)
