n=int(input())
for i in range(n):
    m=int(input())
    p=input()
    q=input()
    pl=[]
    ql=[]
    pv=0
    qv=0
    counter=0
    step=0
    bounter=0
    for i in p:
        pl.append(int(i))
        pv+=int(i)
    for j in q:
        ql.append(int(j))
        qv+=int(j)
    for k in range(len(ql)):
        if pl[k]!=ql[k]:
            if pl[k]==0:
                counter+=1
            else:
                bounter+=1
    print(max(counter,bounter))



