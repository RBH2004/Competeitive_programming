inputs=int(input())
def minus_string():
    initial_string=""
    for i in range(1):
        initial_string=s-s[i]
    return initial_string

for i in range(inputs):
    n1=int(input())
    n2=int(input())
    s=input()
    new_string=""
    sum=n1-n2
    for j in range(n2):
        minus_string()
        for i in range(sum-1,-1,-1):
            new_string+=s[i]
        if new_string==s:
            print("yes,it is a palindrome")
        else:
            print("no,not a palindrome")





