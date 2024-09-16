n=int(input())
for j in range(n):
    m=int(input())
    s=input()
    my_list=s.split(" ")
    final_list=[]
    for i in my_list:
        final_list.append(int(i))
    def sum(a):
        flag=False
        temp=a[0]+a[1]
        for k in range(len(a)-1):
            if a[k]+a[k+1]==temp:
                flag=True
            else:
                flag=False
                break
        return flag
    c=True
    for l in range(len(final_list)-1):
        c=sum(final_list)
        if c==True:
            print("YES")
            break
        else:
            flag=False
            semp=final_list[l]
            final_list[l]=final_list[l+1]
            final_list[l+1]=semp
    if c==False:
        print("NO")



