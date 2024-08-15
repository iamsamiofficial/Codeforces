import math
for _ in range(int(input())):
    n,x = input().split()
    n = int(n)
    x = int(x)
    b = list(map(int,input().split()))
    r = int(1e10)
    l = 0
    
    while l<=r:
        w = 0
        mid = (r+l)//2
        for i in range(len(b)):
            w+= max(mid-b[i],0)
        if w == x:
            break
        elif w>x:
            r = mid-1
        else:
            l = mid+1
    if w>x:
        print(mid-1)
        continue
    print(mid)
