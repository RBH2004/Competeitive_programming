def caller(s):
    my_list=[]
    new_string=""
    for i in range(len(s)):
        if i==0:
            pass
        elif "0"<=s[i]<="9":
            new_string+=s[i]
        elif s[i]==" ":
            my_list.append((new_string))
            new_string=""
    my_list.append((new_string))
    return my_list
n=int(input())
p=input()
p_list=caller(p)
q=input()
q_list=caller(q)
flag=True
for i in range(1,n+1):
    if (str(i) in p_list) or (str(i) in q_list):
        flag=True
    else:
        flag=False
        break
if flag==True:
    print("I become the guy.")
elif flag==False:
    print("Oh, my keyboard!")
