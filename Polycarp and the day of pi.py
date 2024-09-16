
new_string="3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825"
n=int(input())
for j in range(n):
    s1=input()
    counter=0
    for i in range(len(s1)):
        if s1[i]==new_string[i]:
            counter+=1
        else:
            break
    print(counter)
