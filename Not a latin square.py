n=int(input())
for i in range(n):
    my_list=[]
    for i in range(3):
        s=(input())
        my_list.append(s)
    for k in my_list:
        if "?" in k:
            if "A" not in k:
                print("A")
                break
            elif "B" not in k:
                print("B")
                break
            elif "C" not in k:
                print("C")
                break


