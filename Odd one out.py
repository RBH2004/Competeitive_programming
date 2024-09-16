n=int(input())
for i in range(n):
    n1,n2,n3=0,0,0
    s=input()
    new_string=""
    input_list=[]
    for i in range(len(s)):
        if "0"<=s[i]<="9":
            new_string+=s[i]
        elif s[i]==" ":
            input_list.append(int(new_string))
            new_string=""
    input_list.append(int(new_string))
    n1,n2,n3=input_list[0],input_list[1],input_list[2]
    n1c,n2c,n3c=0,0,0
    for i in input_list:
        if i==n1:
            n1c+=1
        elif i==n2:
            n2c+=1
        elif i==n3:
            n3c+=1
    if n1c==1:
        print(n1)
    elif n2c==1:
        print(n2)
    elif n3c==1:
        print(n3)
