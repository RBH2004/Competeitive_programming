s=input()
n=len(s)
s1="hello"
new_string=""
counter=0
string_counter=0
for i in s1:
    for j in range(string_counter,len(s),1):
        if i==s[j]:
            new_string+=s[j]
            string_counter=counter
            counter+=1
            break
        counter+=1
if new_string==s1:
    print("YES")
else:
    print("NO")


