n=int(input())
for i in range(n):
    s=input()
    final_list=s.split(" ")
    my_list=[]
    for k in final_list:
        my_list.append(int(k))
    t=my_list[0]
    counter=0
    for j in range(1,len(my_list),1):
        if my_list[j]>t:
            counter+=1
    print(counter)
