import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    p = [0]
    ns = []
    for i in l:
        p.append(p[-1]+i)

    for i in range(1,n+1):
        mx = 0
        mn = math.inf
        if n%i == 0:
            j = i
            while j <n+1:
                mx = max(mx,p[j]-p[j-i])
                mn = min(mn,p[j]-p[j-i])
                j+=i
        ns.append(mx-mn)
    print(max(ns))
