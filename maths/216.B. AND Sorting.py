import math
for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    mxi = max(p)
    i = 0
    while i<n:
        if p[i]!=i:
            break
        i+=1
    while i<n:
        if p[i]!=i:

            mxi = mxi&p[i]

        i+=1
    print(mxi)