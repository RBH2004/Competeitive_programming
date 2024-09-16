inputs=int(input())
for i in range(inputs):
    user=input()
    if (len(user))<=10:
        print(user)
    else:
        new_string=""
        new_string+=user[0]
        new_string+=str(len(user)-2)
        new_string+=user[len(user)-1]
        print(new_string)
