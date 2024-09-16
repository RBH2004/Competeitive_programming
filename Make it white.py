n=int(input())

for i in range(n):
    m=int(input())
    s=input()
    bc,wc=0,0
    for j in s:
        if j=="W":
            wc+=1
        else:
            bc+=1
    counter=0
    flag=True
    for k in range(len(s)):
        if s[k]=="W" and flag==True:
            continue
        if bc!=0:
            counter+=1
        if s[k]=="B":
            bc-=1
            flag=False

    print(counter)

