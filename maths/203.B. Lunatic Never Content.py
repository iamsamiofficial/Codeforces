import math
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    x = 0
    ns = []
    for i in range(math.ceil(n/2)):
        ns.append(abs(b[i]-b[(n-1)-i]))
    for i in range(len(ns)):
        x = math.gcd(x,ns[i])
    print(x)
