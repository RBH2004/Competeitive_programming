n=int(input())
for i in range(n):
    s=input()
    p=s.split(" ")
    a,b,c=int(p[0]),int(p[1]),int(p[2])
    a_counter,b_counter=0,0
    a_div=a
    b_div=b
    ai=0
    bi=0
    flag=False
    while True:
        if a_div%2==0:
            a_div=a_div/2
            ai+=1
        else:
            a_counter=2**ai
            break
    while True:
        if b_div%2==0:
            b_div=b_div/2
            bi+=1
        else:
            b_counter=2**bi
            break
    counter=int(a_counter*b_counter)

    if counter>=c:
        print("YES")
    else:
        print("NO")
