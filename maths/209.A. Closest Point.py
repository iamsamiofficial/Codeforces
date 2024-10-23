for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    b.sort()
    c = b[1]-1
    d = 0
    if c == b[0]:
        print("NO")
        continue
    for i in range(1,n):
        if b[i]-c> b[i]-b[i-1]:
            d = 1
            break
    if d == 1:
        print("NO")
        continue
    print("YES")