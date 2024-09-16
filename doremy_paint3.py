n=int(input())
for j in range(n):
    m=int(input())
    s=input()
    my_list=s.split(" ")
    final_list=[]
    for i in my_list:
        final_list.append(int(i))
    counter=0
    flag=False
    for a in range(len(final_list)):
        for b in range(len(final_list)-1):
            temp=final_list[b]
            final_list[b]=final_list[b+1]
            final_list[b+1]=temp
            sum=final_list[0]+final_list[1]
            for c in range(len(final_list)-1):
                if final_list[c]+final_list[c+1]==sum:
                    flag=True
                else:
                    flag=False
                    break
            if flag==True:
                break
        if flag==True:
            print("YES")
            break
    if flag==False:
        print("NO")






