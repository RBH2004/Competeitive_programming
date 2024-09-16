n=int(input())
s=input()
def lo_counter(m):
    lc=0
    oc=0
    for i in m:
        if i=="L":
            lc+=1
        else:
            oc+=1
    return lc,oc
counter=1
p=""
q=""
flag=False
for i in range(n):
    p+=s[i]
    q=s[i+1::]
    r1,d1=lo_counter(p)
    r2,d2=lo_counter(q)
    if r1!=r2 and d1!=d2 and counter!=n:
        flag=True
        ans=counter
        break
    else:
        counter+=1
        flag=False
if flag==True:
    print(ans)
elif flag==False:
    print("-1")



