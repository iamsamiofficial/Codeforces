import math
for _ in range(int(input())):
    n = int(input())
    if n&(n-1) == 0:
        print("NO")
        continue
    print("YES")
    
