import math
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    c = [0]
    ns = 0
    for i in b:
        c.append(c[-1]+i)
    
    for i in range(len(c)-2,0,-1):
        ns = max(ns,(math.gcd(c[i],(c[-1]-c[i]))))
    print(ns)