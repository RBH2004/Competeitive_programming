p=input()
q=input()
r=""
n=""
sump=0
sumq=0
counter=0
for i in range(len(p)):
    m=ord(p[i])
    if 65<=m<=90:
        m+=32
        r+=chr(m)
    else:
        r+=chr(m)
for i in range(len(q)):
    m=ord(q[i])
    if 65<=m<=90:
        m+=32
        n+=chr(m)
    else:
        n+=chr(m)
for i in r:
    m=ord(i)
    sump+=m
for i in n:
    m=ord(i)
    sumq+=m
if sump==sumq:
    pass
elif sump>sumq:
    counter+=1
elif sump<sumq:
    counter-=1
print(len(r),len(n))
print(counter)
