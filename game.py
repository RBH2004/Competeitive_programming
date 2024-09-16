n=int(input("Please enter how many games you want to play :"))
for i in range(n):
    s=input()
    if s==".":
        print(f"You have decided to finish the game")
        break
    else:
        if s=="=":
            for i in range(1,5+1,1):
                for j in range(i+1):
                    print("*",end="")
                print()
        elif s=="-":
            for i in range(1,5+1,1):
                for j in range(i+1):
                    print("#",end="")

