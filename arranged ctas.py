def solve():
    n = int(input())
    s = input().strip()
    t = input().strip()
    a = b = 0
    for i in range(n):
        if s[i] != t[i]:
            if s[i] == '0':
                a += 1
            else:
                b += 1

    ans = max(a, b)
    print(ans)

def main():
    t = int(input())

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
