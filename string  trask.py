s=input()
ls=""
vowels="aeiouy"
cs=""
fs=""
for i in range(len(s)):
    m=ord(s[i])
    if 65<=m<=90:
        m+=32
        ls+=chr(m)
    else:
        ls+=chr(m)
for i in ls:
    if i in vowels:
        pass
    else:
        cs+=i
for i in cs:
    fs+="."+i
print(fs)
