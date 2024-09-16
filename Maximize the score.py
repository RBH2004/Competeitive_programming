n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    p=s.split(" ")
    q=[]
    for i in p:
        q.append(int(i))
    counter=1
    sum=0
    i=0
    while counter<=len(q)//2:
        sum+=min(q[i],q[i+1])
        counter+=1
        i+=2

    print(sum)
