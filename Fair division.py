n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    p=s.split(" ")
    q=[]
    for i in range(m):
        q.append(int(p[i]))
    oc=0
    tc=0
    if "2" not in s:
        for i in q:
            if i==1:
                oc+=1
        if oc%2==0:
            print("YES")
        else:
            print("NO")
    elif "1" not in s:
        for i in q:
            if i==2:
                tc+=1
        if tc%2==0:
            print("YES")
        else:
            print("NO")
    else:
        counter=0
        for k in q:
            counter+=k
            if k==1:
                oc+=1
            else:
                tc+=1
        if oc%2==0 and tc%2==0 and oc >1 and tc>1:
            print("YES")
        elif counter%2==0:
            print("YES")
        else:
            print("NO")




