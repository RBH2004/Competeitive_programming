n=int(input())
for i in range(n):
    s=input()
    l=s.split(" ")
    n,f,k=int(l[0]),int(l[1]),int(l[2])
    d=input()
    dl=d.split(" ")
    m=[]

    for i in range(len(dl)):
        m.append(int(dl[i]))
    need=m[f-1]
    need_counter=0
    for i in range(len(m)):
        if need==m[i]:
            need_counter+=1
    m.sort(reverse=True)
    final=[]
    less_final=[]
    for i in range(k):
        final.append(m[i])
    if (n-k)>1:
        for i in range(k,len(s),1):
            less_final.append(m[i])
    if need in final:
        if need in less_final:
            print("MAYBE")
        else:
            print("YES")
    else:
        print("NO")

