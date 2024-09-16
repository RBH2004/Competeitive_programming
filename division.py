n=int(input())
for i in range(n):
    m=int(input())
    if m<=1399:
        print("Division 4")
    elif 14<=m<=1599:
        print("Division 3")
    elif 1600<=m<=1899:
        print("Division 2")
    elif m>=1900:
        print("Division 1")
