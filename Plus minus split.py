n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    counter=0
    for j in s:
        if j=="+":
            counter+=1
        elif j=="-":
            counter-=1
    print(abs(counter))
