n=int(input())
for j in range(n):
    s=input()
    new_string=""
    for i in range(len(s)):
        m=ord(s[i])
        if 65<=m<=90:
            m+=32
            new_string+=chr(m)
        elif 97<=m<=122:
            new_string+=chr(m)
    if new_string=="yes":
        print("YES")
    else:
        print("NO")
