p=input()
q=input()
r=""
for i in range(len(p)):
    if p[i]==q[i]:
        r+="0"
    else:
        r+="1"
print(r)
