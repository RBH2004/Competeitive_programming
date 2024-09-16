m=int(input())
for i in range(m):
    n=int(input())
    my_list=[]
    flag=True
    for i in range(1,n,1):
        if i%3==0:
            continue
        my_list=[]
        for j in range(1,n,1):
            if j==i or (i%3==0 or j%3==0):
                continue
            for k in range(1,n,1):
                if k==j or k==i or k%3==0 or i%3==0 or j%3==0:
                    continue
                if i+j+k==n:
                    my_list.append(i)
                    my_list.append(j)
                    my_list.append(k)
                    flag=False
                    break
                if flag==False:
                    break
            if flag==False:
                break
        if flag==False:
            break
    if len(my_list)==3:
        print("YES")
        for i in my_list:
            print(i,end=" ")
        print()
    else:
        print("NO")
