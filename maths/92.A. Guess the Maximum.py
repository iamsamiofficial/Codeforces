


import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    
    ans = []
    
    for i in range(n - 1):
        max_pair = max(a[i], a[i + 1])
        ans.append(max_pair)
    
    ansi = min(ans)
    print(ansi-1)


