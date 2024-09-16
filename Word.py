s=input()
u_counter=0
s_counter=0
new_string=""
for i in s:
    if "A"<=i<="Z":
        u_counter+=1
    elif "a"<=i<="z":
        s_counter+=1
if u_counter>s_counter:
    for i in range(len(s)):
        m=ord(s[i])
        if 65<=m<=90:
            new_string+=chr(m)
        elif 97<=m<=122:
            m-=32
            new_string+=chr(m)
elif s_counter>u_counter:
    for i in range(len(s)):
        m=ord(s[i])
        if 65<=m<=90:
            m+=32
            new_string+=chr(m)
        elif 97<=m<=122:
            new_string+=chr(m)
elif s_counter==u_counter:
    for i in range(len(s)):
        m=ord(s[i])
        if 65<=m<=90:
            m+=32
            new_string+=chr(m)
        elif 97<=m<=122:
            new_string+=chr(m)
print(new_string)
