n=int(input())
counter=0
for i in range(n):
    s=input()
    if s=="++X" or s=="X++":
        counter+=1
    elif s=="--X" or s=="X--":
        counter-=1
print(counter)
