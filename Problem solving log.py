n=int(input())
for i in range(n):
    p=int(input())
    s=input()
    counter=0
    my_list=[]
    final_list=[]
    for j in s:
        my_list.append(j)
    for k in my_list:
        if k not in final_list:
            final_list.append(k)
    for l in final_list:
        l_num=ord(l)-65+1
        l_count=0
        for n in my_list:
            if l==n:
                l_count+=1
        if l_count>=l_num:
            counter+=1
    print(counter)
