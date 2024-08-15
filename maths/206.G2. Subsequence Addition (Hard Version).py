for _ in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    c.sort()
    ns = 0
    if c[0] != 1:
        print("NO")
        continue
    s = c[0]
    for i in range(1,n):
        if c[i]>s:
            ns = 1
            break
        s+=c[i]
    if ns == 1:
        print("NO")
        continue
    print("YES")