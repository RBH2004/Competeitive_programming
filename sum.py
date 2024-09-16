n=int(input())
for i in range(n):
    s=input()
    new_string=""
    my_list=[]
    for i in range(len(s)):
        if s[i]==" ":
            my_list.append(int(new_string))
            new_string=""
        elif "0"<=s[i]<="9":
            new_string+=s[i]
    my_list.append(int(new_string))
    a,b,c=my_list[0],my_list[1],my_list[2]
    counter=0
    if a==(b+c):
        counter+=1
    elif b==(a+c):
        counter+=1
    elif c==(a+b):
        counter+=1
    if counter>=1:
        print("YES")
    else:
        print("NO")

