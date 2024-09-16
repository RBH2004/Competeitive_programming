n=int(input())
s=input()
global counter=0
def x_counter(a):
    for i in range(counter,len(a)):
        if s[i]=="x" and s[i+1]=="x":
            counter+=1
        elif s[i]!="x":
            counter+=1
            break
    return counter
bounter=0
for i in range(len(s)):
    if s[i]=="x":
        num_x=x_counter(s)


