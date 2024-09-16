n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    a_counter,b_counter,c_counter,d_counter=0,0,0,0
    for i in range(len(s)):
        if s[i]=="A" and a_counter<m:
            a_counter+=1
        elif s[i]=="B" and b_counter<m:
            b_counter+=1
        elif s[i]=="C" and c_counter<m:
            c_counter+=1
        elif s[i]=="D" and d_counter<m:
            d_counter+=1
    print(a_counter+b_counter+c_counter+d_counter)
