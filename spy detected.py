n=int(input())
for v in range(n):
    m=int(input())
    s=input()
    my_list=s.split(" ")
    final_list=[]
    counter=0
    for k in my_list:
        if k not in final_list:
            final_list.append(k)
    for l in final_list:
        counter=0
        for j in range(len(my_list)):
            if l==my_list[j]:
                counter+=1
                index=j
        if counter==1:
            print(index+1)
            break
        else:
            continue

