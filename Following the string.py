n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    p=s.split(' ')
    q=[]
    for i in p:
        q.append(int(i))
    def lister(pl,sl):
        counter=0
        for i in pl:
            if i==str(sl):
                counter+=1
        return counter
    zero,one,two,three,four,five,six,seven,eight,nine=lister(p,0),lister(p,1),lister(p,2),lister(p,3),lister(p,4),lister(p,5),lister(p,6),lister(p,7),lister(p,8),lister(p,9)
    m=97
    s=""
    for i in range(zero):
        s+=chr(m)
        m+=1
    for i in range(one):
        temp=s
        s+=temp[i]
    for i in range(two):
        temp=s
        s+=temp[i]
    for i in range(three):
        temp=s
        s+=temp[i]
    for i in range(four):
        temp=s
        s+=temp[i]
    for i in range(five):
        temp=s
        s+=temp[i]
    for i in range(six):
        temp=s
        s+=temp[i]
    for i in range(seven):
        temp=s
        s+=temp[i]
    for i in range(eight):
        temp=s
        s+=temp[i]
    for i in range(nine):
        temp=s
        s+=temp[i]
    print(s)


