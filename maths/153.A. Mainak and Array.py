import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    maxi = max(a[-1]-min(a),max(a)-a[0])
    for i in range(n-1):
        maxi = max(maxi,a[i]-a[i+1])
    print(maxi)

