
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    a = []
    for i in l:
        a.append((n+1)-i)
    print(*a)