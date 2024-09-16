n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    q=[]
    for j in p:
        q.append(int(j))
    a,b=int(q[0]),int(q[1])
    new_string=""
    for i in range(a):
        m=97
        for j in range(b):
            new_string+=chr(m)
            m+=1
    print(new_string)

