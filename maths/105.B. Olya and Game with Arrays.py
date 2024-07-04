import math
for _ in range(int(input())):
    mini = math.inf
    final = []
    for _ in range(int(input())):
        m = int(input())
        l = list(map(int,input().split()))
        l.sort()
        mini = min(mini,l[0])
        final.append(l[1])
    final.sort()
    ans = sum(final[1:])+mini
    print(ans)