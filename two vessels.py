n=int(input())
for i in range(n):
    s=input()
    ml=s.split(" ")
    fl=[]
    for j in ml:
        fl.append(int(j))
    p,q,r=fl[0],fl[1],fl[2]
    if p==q:
        print(0)
    elif p<q and p+r==q-r:
        print(1)
    elif q<p and q+r==p-r:
        print(1)
    else:
        counter=0
        if p<q:
            while True:
                if p==q:
                    break
                elif p+r==q-r:
                    p+=r
                    q-=r
                    counter+=1
                elif (q-p)//2<=r:
                    p+=(q-p)//2
                    q-=(q-p)//2
                    counter+=1
                else:
                    p+=r
                    q-=r
                    counter+=1
            print(counter)
        elif p>q:
            while True:
                if q==p:
                    break
                elif q+r==p-r:
                    q+=r
                    p-=r
                    counter+=1
                elif (p-q)//2<=r:
                    q+=(p-q)//2
                    p-=(p-q)//2
                    counter+=1
                else:
                    q+=r
                    p-=r
                    counter+=1
            print(counter)
