vowels="aeiouy"
s=input()
new_string=""
for i in range(len(s)):
    m=ord(s[i])
    if s[i]=="?":
        pass
    elif 65<=m<=90:
        m+=32
        new_string+=chr(m)
    elif 97<=m<=122:
        new_string+=chr(m)
if new_string[len(new_string)-1] in vowels:
    print("YES")
else:
    print("NO")
