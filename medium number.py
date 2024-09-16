n=int(input())
for j in range(n):
    s=input()
    my_list=s.split(" ")
    final_list=[]
    for i in my_list:
        final_list.append(int(i))
    a,b,c=final_list[0],final_list[1],final_list[2]
    if b<a<c or c<a<b:
        print(a)

    elif a<b<c or c<b<a:
        print(b)

    else:
        print(c)


