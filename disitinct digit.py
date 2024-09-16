n=int(input())
while True:
    n+=1
    s=str(n)
    my_list=[]
    for i in range(len(s)):
        if s[i] not in my_list:
            my_list.append(s[i])
        elif s[i] in my_list:
            break
    if len(my_list)==len(s):
        print(n)
        break
    else:
        continue
