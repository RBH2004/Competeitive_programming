m=int(input())
for j in range(m):
    s=input()
    my_list=s.split(" ")
    n1,n2=int(my_list[0]),int(my_list[1])
    counter=0
    bounter=0
    num=0
    while True:
        if n1%n2==0:
            print(counter)
            break
        elif bounter>=1:
            print(counter)
            break
        else:
            temp=n1
            n1+=n2
            rest=n1%n2
            counter=n1-rest-temp
            bounter+=1


