n=int(input())
for i in range(n):
    s=input()
    m=[]
    d=input()
    for _ in d:
        m.append(_)
    my_list=s.split(" ")
    p,q=int(my_list[0]),int(my_list[1])
    x=0
    def b_counter(g):
        b=0
        for j in g:
            if j=="B":
                b+=1
        return b
    v=b_counter(m)
    if v==q:
        print("0")
    elif v!=q:
        if v==0:
            print("1")
            print(q,"B")
        elif v>q:
            for k in range(len(m)):
                m[k]="A"
                x+=1
                if b_counter(m)==q:
                    print("1")
                    print(x,"A")
                    break
                elif b_counter(m)>q:
                    continue
        elif v<q:
            for k in range(len(m)):
                m[k]="B"
                x+=1
                if b_counter(m)==q:
                    print("1")
                    print(x,"B")
                    break
                elif b_counter(m)<q:
                    continue



