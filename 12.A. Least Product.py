import math
t = int(input())
for _ in range(t):
    n = int(input())
    j = list(map(int,input().split()))
    r = math.prod(j)

    if r >0:
        print(1)
        print(1,0)
    else:
        print(0)


    