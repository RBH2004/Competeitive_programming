k,l,m,n=int(input()),int(input()),int(input()),int(input())
d=int(input())
if k==1 or l==1 or m==1 or n==1:
    print(d)
else:
    def caller(p,s):
        my_list=[]
        for i in range(p,s+1,p):
            my_list.append(i)
        return my_list
    k_l=caller(k,d)
    l_l=caller(l,d)
    m_l=caller(m,d)
    n_l=caller(n,d)
    final_list=k_l+l_l+m_l+n_l
    u_list=[]
    for i in final_list:
        if i not in u_list:
            u_list.append(i)
    print(len(u_list))

