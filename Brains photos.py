p=input()
pl=p.split(" ")
m,n=int(pl[0]),int(pl[1])
my_list=[]
for i in range(m):
    s=input()
    my_list+=s.split(" ")
c="CMY"
flag=False
for i in c:
    if i in my_list:
        flag=True
        break
if flag==True:
    print("#Color")
else:
    print("#Black&White")
