for _ in range(int(input())):
    d = {}
    n = int(input())
    b = list(map(int,input().split()))
    for i in b:
        d[i] = (n-1)
    c = sorted(b)
    
    f = 0
    pre = []
    for i in range(n-1):
        pre.append(f+c[i])
        f+=c[i]

    p = 0
    for i in range(len(pre)-1,-1,-1):
        if pre[i] >= c[i+1]:
            d[c[i]] = d[c[i+1]]
        else:
            d[c[i]] = i

    for i in b:
        print(d[i],end=" ")
    print()
    
