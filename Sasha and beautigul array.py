n=int(input())
for i in range(n):
    m,s=int(input()),input()
    p=s.split(" ")
    q,sum=[],0
    for i in p:
        q.append(int(i))
    q.sort()
    for i in range(1,len(q),1):
        sum+=q[i]-q[i-1]
    print(sum)
