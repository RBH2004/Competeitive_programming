n=int(input())
for i in range(n):
    s=input()
    new_string=""
    a,b=0,0
    for i in s:
        if "0"<=i<="9":
            new_string+=i
        elif i==" ":
            a=int(new_string)
            new_string=""
    b=int(new_string)
    if (a+b)%2==0:
        print("Bob")
    else:
        print("Alice")
