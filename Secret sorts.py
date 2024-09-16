n=int(input())
for k in range(n):
    m=int(input())
    s=input()
    ac=0
    bc=0
    for j in s:
        if j=="A":
            ac+=1
        else:
            bc+=1
    flag=False
    if "A" not in s:
        flag=True
        ans="B"
    elif "B" not in s:
        flag=True
        ans="A"
    elif ("A" in s) and ("B" in s):
        for i in range(m-1):
            if s[0]=="B" and s[1]=="B":
                ans="A"
                flag=True
            elif s[0]=="A" and s[1]=="A":
                ans="B"
                flag=True
    if flag==False:
        if ac>bc:
            ans=("A")
        else:
            ans=("B")
    print(ans)

