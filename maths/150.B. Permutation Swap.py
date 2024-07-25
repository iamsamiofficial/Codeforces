import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    j = []
    ans = 0
    for i in range(len(a)):
        ans = math.gcd(ans,a[i]-(i+1))
    print(ans)