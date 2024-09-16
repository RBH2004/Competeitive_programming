n=int(input())
my_list=[]
if n==1:
    print(1)
else:
    for j in range(n):
        if j==0:
            for i in range(n):
                my_list.append(1)

        else:
            m=len(my_list)
            final_list=[]
            counter=1
            final_list.append(1)
            for i in range(1,len(my_list),1):
                counter+=my_list[i]
                final_list.append(counter)

            my_list=final_list
    print(my_list[n-1])


