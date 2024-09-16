n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    q=[]
    p=s.split(" ")
    oc,zc=0,0
    for i in p:
        if i=="0":
            zc+=1
        else:
            oc+=1
        q.append(int(i))
    sum,counter=0,0
    for i in range(len(q)):
        if counter==oc:
            break
        else:
            if q[i]==1:
                counter+=1
            else:
                sum+=1
    if q[0]==0:
        sum-=1
    print(sum)


