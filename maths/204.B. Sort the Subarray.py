import math
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    g = 0
    h = 0
    for i in range(n):
        if b[i]!= c[i]:
            g = i
            break
    for i in range(n-1,-1,-1):
        if b[i]!= c[i]:
            h = i
            break
    for i in range(g,0,-1):
        if c[i] >= c[i-1]:
            g = i-1
        else:
            break
    for i in range(h,n-1):
        if c[i]<= c[i+1]:
            h = i+1
        else:
            break
    print(g+1,h+1)


