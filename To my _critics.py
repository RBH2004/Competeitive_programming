n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    q=[]
    for i in p:
        q.append(int(i))
    flag=False
    for j in range(len(q)):
        sum=0
        for k in range(len(q)):
            if j==k:
                continue
            else:
                if q[j]+q[k]>=10:
                    flag=True
                    break
        if flag==True:
            break
    if flag==True:
        print("YES")
    else:
        print("NO")
