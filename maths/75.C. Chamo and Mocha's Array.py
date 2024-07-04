import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = min(l)
    for i in range(len(l)-2):
        a,b,c = sorted(l[i:i+3])
        d = max(d,b)
    print(d)
