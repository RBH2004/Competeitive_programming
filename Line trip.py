n=int(input())
for i in range(n):
    s=input()
    m=input()
    sl=s.split(" ")
    p,q=int(sl[0]),int(sl[1])
    ml=m.split(" ")
    final_list=[0]
    for k in ml:
        final_list.append(int(k))
    nf=len(final_list)
    max=0
    if len(ml)==1:
        for i in range(2):
            if i==0:
                ans=int(ml[0])
                if ans>max:
                    max=ans
            else:
                ans=2*(q-int(ml[0]))
                if ans>max:
                    max=ans
    else:
        for i in range(nf):
            if i==(nf-1):
                ans=2*(q-final_list[i])
                if ans>max:
                    max=ans
            else:
                ans=final_list[i+1]-final_list[i]
                if ans>max:
                    max=ans
    print(max)

