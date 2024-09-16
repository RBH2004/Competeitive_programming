n=int(input())
for i in range(n):
    n=int(input())
    if n==2 or (n//2)%2!=0:
        print("NO")
    else:
        i=1
        ol=[]
        el=[]
        while True:
            if len(ol)==(n//2) and len(el)==(n//2):
                break
            if i%2!=0:
                ol.append(i)
            if i%2==0:
                el.append(i)
            i+=1
        print("YES")
        for i in el:
            print(i,end=" ")
        for j in ol:
            print(j,end=" ")
        print()



