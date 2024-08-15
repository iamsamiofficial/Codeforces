for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    b = [0]
    for i in l:
        b.append(b[-1]+i)
    ns = 0

    for i in range(k+1):
        ns = max(ns,b[n-i]-b[2*(k-i)])

    print(ns)