n=int(input())
for i in range(n):
    s=input()
    my_list=s.split(" ")
    d=[]
    for i in my_list:
        d.append(int(i))
    a,b,c=d[0],d[1],d[2]
    if a+b==c:
        print("+")
    elif a-b==c:
        print("-")


