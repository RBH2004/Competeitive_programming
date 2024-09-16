s= input("Please enter your input :")
letter_counter=0
number_counter=0
other=0
for i in range(len(s)):
    m=ord(s[i])
    if 48<=m<=57:
        number_counter+=1
    elif 97<=m<=122 or 65<=m<=90:
        letter_counter+=1
    else:
        other+=1
if number_counter==0 and letter_counter!=0 and other==0:
    print("Only Letters")
elif number_counter!=0 and letter_counter==0 and other==0:
    print("omly numbers")
else:
    print("Mixed")
