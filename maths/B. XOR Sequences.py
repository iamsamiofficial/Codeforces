
# import math
# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     p = 1
#     ans = []
#     for i in range(len(l)):
#         q = math.gcd(p,l[i])
#         r = l[i]//q
#         p*=r

#     t = 0
#     for i in range(len(l)):
#         t+=p//l[i]
#         m = p//l[i]
#         ans.append(m)
#     if t>=p:
#         print(-1)
#     else:
#         print(*ans)
# for _ in range(int(input())):
#     x,y = map(int,input().split())
#     xy = x^y
#     l = 1
#     while (xy%2 == 0):
#         xy>>=1
#         l<<=1
#     print(l)

import math
for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    lcm = math.lcm(*l)
    ans = []
    
    for i in l:
        ans.append(lcm//i)
    if sum(ans)<lcm:
        print(*ans)
    else:
        print(-1)
