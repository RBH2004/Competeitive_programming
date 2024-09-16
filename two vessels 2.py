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
    elif abs((p-q))<=r or abs((q-p))<=r:
        print(1)
    elif p+r==q-r or q+r==p-r:
        print(1)

    elif p>q:
        if ((p-q)/2)%2==0 or ((p-q)/2)==1 :
            print(int(((p-q)//2)/r))
        else:
            print(int(((p-q)//2)/r)+1)
    elif q>p:
        if ((p-q)/2)%2==0 or ((q-p)/2)==1:
            print(int(((q-p)//2)/r))
        else:
            print(int(((q-p)//2)/r)+1)
