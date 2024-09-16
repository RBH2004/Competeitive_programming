s=input()
new_string=""
for i in s:
    if i not in new_string:
        new_string+=i
n=len(new_string)
if n%2==0:
    print( "CHAT WITH HER!")
else:
    print("IGNORE HIM!")
