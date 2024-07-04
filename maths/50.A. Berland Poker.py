
import math
for _ in range(int(input())):
    n,m,k = map(int,input().split())
    j = n//k
    if j>=m:
        print(m)
    else:
        a = m-j
        f = math.ceil(a/(k-1))
        print(j-f)