n=int(input())
my_list=[]
counter=0
for i in range(1,n+1):
    if counter==0:
        if n==1:
            my_list.append("I hate it")
        else:
            my_list.append("I hate that")
        counter+=1
    else:
        if my_list[i-1-1]=="I hate that" and i!=n:
            my_list.append("I love that")
        elif my_list[i-1-1]=="I love that" and i!=n:
            my_list.append("I hate that")
        elif my_list[i-1-1]=="I hate that" and i==n:
            my_list.append("I love it")
        elif my_list[i-1-1]=="I love that" and i==n:
            my_list.append("I hate it")
final=""
for i in range(len(my_list)):
    if i==(len(my_list)-1):
        final+=my_list[i]
    else:
        final+=my_list[i]+" "
print(final)


