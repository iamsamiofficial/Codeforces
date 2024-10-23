for _ in range(int(input())):
    n,l,r = map(int,input().split())
    ns = []

    for i in range(1,n+1):
        if l%i == 0:
            ns.append(l)
        else:
            ns.append(l+(i-(l%i)))
    if ns:
        p = sorted(ns)
    if not ns or p[-1]>r:
        print("NO")
        continue
    print("YES")
    print(*ns)

