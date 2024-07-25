# import math
# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     a = list(map(int,input().split()))
#     j =(n*k)- (math.floor(n/2)+1)
#     ans = 0
#     for _ in range(k):
#         ans+=a[j]
#         j -= (math.floor(n/2)+1)
#     print(ans)

import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    j =- (math.floor(n/2)+1)
    ans = 0
    for _ in range(k):
        ans+=a[j]
        j -= (math.floor(n/2)+1)
    print(ans)