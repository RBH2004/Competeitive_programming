n=int(input())
for i in range(n):
    s=input()
    new_string=""
    for i in range(len(s)):
        if i==0 or i%2!=0:
            new_string+=s[i]
        else:
            pass
    print(new_string)
