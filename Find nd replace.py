p=int(input())
for i in range(p):
    flag=True
    q=int(input())
    s=input()
    my_list=[]
    for i in range(q-1):
        if s[i] not in my_list:
            my_list.append(s[i])
        if s[i]!=s[i+1]:
            flag=True
        elif s[i]==s[i+1]:
            flag=False
            break

    if flag==True and len(my_list)<=4:
        print("YES")
    elif len(s)==1:
        print("YES")
    else:
        print("NO")

