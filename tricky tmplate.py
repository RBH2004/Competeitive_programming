n=int(input())
for i in range(n):
    m=int(input())
    p=input()
    q=input()
    r=input()
    counter=0
    for j in range(m):
        if p[j]!=r[j] and q[j]!=r[j]:
            counter+=1
            print("YES")
            break
    if counter==0:
        print("NO")

