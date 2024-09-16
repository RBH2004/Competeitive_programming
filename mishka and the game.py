n=int(input())
m=0
c=0
for i in range(n):
    s=input()
    my_list=s.split(" ")
    final_list=[]
    for i in my_list:
        final_list.append(int(i))
    p,q=final_list[0],final_list[1]
    if p>q:
        m+=1
    elif q>p:
        c+=1
if m>c:
    print("Mishka")
elif c>m:
    print("Chris")
else:
    print("Friendship is magic!^^")
