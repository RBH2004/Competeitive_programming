s=input()
s1=input()
new_string=""
for i in range(len(s1)-1,-1,-1):
    new_string+=s1[i]
if new_string==s:
    print("YES")
else:
    print("NO")
