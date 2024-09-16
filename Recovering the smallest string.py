n=int(input())
for i in range(n):
    m=int(input())
    p,q,r=0,0,0
    p=int(m//3)+96
    q=p
    r=p+int(m%3)
    new_string=chr(p)+chr(q)+chr(r)
    print(new_string)
