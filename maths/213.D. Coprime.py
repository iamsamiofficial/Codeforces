import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    # i = len(l)-1
    # ns = -1
    # while i>=0:
    #     for j in range(i,-1,-1):
    #         if math.gcd(l[i],l[j]) == 1:
    #             ns = max(ns,(i+j+2))
    #             break
    #     i-=1
    # print(ns)

    b = [0]*1001
    for i in range(n):
        b[l[i]] = i+1
    ns = -1
    for i in range(1000,0,-1):
        if b[i]>0:
            for j in range(i,0,-1):
                if b[j]>0 and math.gcd(i,j) == 1:
                    ns = max(ns,b[i]+b[j])
    print(ns)
