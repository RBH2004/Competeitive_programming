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
    if a==b:
        print("Bob")
    elif a>b:
        i=1
        while True:
            if i%2!=0:
                if a!=0 and b==0:
                    print("Alice")
                    break
                elif a==0 and b!=0:
                    print("Bob")
                    break
                else:
                    if a>b:
                        a-=1
                        i+=1
                    elif a<=b:
                        temp=b
                        b=a
                        a=temp
                        a-=1
                        i+=1
            elif i%2==0:
                if b!=0 and a==0:
                    print("Bob")
                    break
                elif b==0 and a!=0:
                    print("Alice")
                    break
                else:
                    if b>a:
                        b-=1
                        i+=1
                    elif b<=a:
                        temp=b
                        b=a
                        a=temp
                        b-=1
                        i+=1
    elif b>a:
        i=1
        while True:
            if i%2!=0:
                if a!=0 and b==0:
                    print("Alice")
                    break
                elif a==0 and b!=0:
                    print("Bob")
                    break
                else:
                    if a>b:
                        a-=1
                        i+=1
                    elif a<=b:
                        temp=b
                        b=a
                        a=temp
                        a-=1
                        i+=1
            elif i%2==0:
                if b!=0 and a==0:
                    print("Bob")
                    break
                elif b==0 and a!=0:
                    print("Alice")
                    break
                else:
                    if b>a:
                        b-=1
                        i+=1
                    elif b<=a:
                        temp=b
                        b=a
                        a=temp
                        b-=1
                        i+=1
