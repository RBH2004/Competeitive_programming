s=input()
counter=0
if len(s)>=5:
    counter+=1
for i in s:
    if "A"<=i<="Z":
        counter+=1
        break
for i in s:
    if "a"<=i<="z":
        counter+=1
        break
for i in s:
    if "0"<=i<="9":
        counter+=1
        break
if counter==4:
    print("Correct")
else:
    print("Too weak")


