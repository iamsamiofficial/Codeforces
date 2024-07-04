import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = sorted(range(len(a)), key=lambda i: a[i], reverse=True)[:3]
    e = sorted(range(len(b)), key=lambda i: b[i], reverse=True)[:3]
    f = sorted(range(len(c)), key=lambda i: c[i], reverse=True)[:3]
    
    s = -math.inf
    for i in range(len(d)):
        for j in range(len(e)):
            if e[j]!=d[i]:
                for k in range(len(f)):
                    if f[k]!=d[i] and f[k]!=e[j]:
                        s = max(s,int(a[d[i]])+int(b[e[j]])+int(c[f[k]]))
    print(s)
            