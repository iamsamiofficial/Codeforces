
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    c = 0
    for i in range(n):
        if a[i]>-1