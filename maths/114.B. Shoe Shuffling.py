# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     if n == 1:
#         print(-1)
#         continue
#     if l[0]!=l[-1]:
#         print(-1)
        
#     else:
#         if n%2 == 0:
#             ans = list(range(n,0,-1))
#             print(*ans)
#         else:
#             ans = list(range(n,0,-1))
#             j = (n//2)
#             ans[0],ans[j] = ans[j],ans[0]
#             print(*ans)
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = input().split()
    
    b = []
    m = 1
    p = 0
    c = Counter(a)
   
    if n == 1 or min(c.values()) ==1:
        print(-1)
        continue
    for i in range(1,n):
        if a[i] == a[i-1]:
            b.append(i+1)
        else:
            b.append(p+1)
            p = i
    b.append(p+1)
    print(*b)


