import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    if n == 1:
        print(k)
    else:
        b = int(math.log2(k))
        a = (2**b) - 1
        c = k-a
        print(a,c,*([0]*(n-2)))