n=int(input())
for i in range(n):
    new_string=""
    m=int(input())
    s=input()
    p=0
    for j in range(m):
        if j==0:
            if s[j]=="1" and s[j+1]=="1":
                p=int(s[j])-int(s[j+1])
                new_string+="-"
            else:
                p=int(s[j])+int(s[j+1])
                new_string+="+"
            continue
        if j==1:
            continue
        if s[j]=="0":
            p+=int(s[j])
            new_string+="+"
        elif p==0 and s[j]=="1":
            p+=int(s[j])
            new_string+="+"
        elif p==1 and s[j]=="1":
            p-=int(s[j])
            new_string+="-"
    print(new_string)
