s=input()
new_string=""
for i in range(len(s)):
    m=ord(s[i])
    if i==0:
        if "A"<=s[i]<="Z":
            new_string+=chr(m)
        elif "a"<=s[i]<="z":
            m-=32
            new_string+=chr(m)
    else:
        new_string+=chr(m)
print(new_string)
