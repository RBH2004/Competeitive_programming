n=int(input())
for i in range(n):
    x=[]
    y=[]
    dl=0
    ll=0
    for j in range(4):
        s=input()
        my_list=s.split(" ")
        x.append(int(my_list[0]))
        y.append(int(my_list[1]))
    for k in range(len(x)):
        if k==0:
            continue
        elif x[0]==x[k]:
            dl=abs(y[k]-y[0])
            break
    for l in range(len(y)):
        if l==0:
            continue
        elif y[0]==y[l]:
            ll=abs(x[l]-x[0])
            break
    print(int(dl*ll))




