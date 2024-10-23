import math
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    s = 0
    c = 0
    ms = math.inf
    for i in b:
        if i<0:
            c+=1
        s+=abs(i)
        ms = min(ms,abs(i))

    if c&1:
        print(s-(2*ms))
        continue
    print(s)
    # c = []
    # for i in range(n):
    #     if b[i]<0:
    #         c.append(i)
    #         b[i] = abs(b[i])
    # b.sort(reverse=True)
    # for i in c:
    #     b[i] = -b[i]
    # for i in range(n-1):
    #     if b[i]<0:
    #         b[i] = abs(b[i])
    #         if b[i+1]<0:
    #             b[i+1] = abs(b[i+1])
    #         else:
    #             b[i+1] = -(b[i+1])
    # print(sum(b))

