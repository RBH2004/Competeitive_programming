n=int(input())
s=input()
anton_counter=0
danik_counter=0
for i in s:
    if i=="A":
        anton_counter+=1
    elif i=="D":
        danik_counter+=1
if anton_counter>danik_counter:
    print("Anton")
elif danik_counter>anton_counter:
    print("Danik")
else:
    print("Friendship")
