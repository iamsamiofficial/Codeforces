import math
for _ in range(int(input())):
    n = int(input())
    c = math.inf
    l = list(map(int,input().split()))
    j = 1
    while j < n:
        if l[j]!=l[0]:
            c = min(c,j)
            break
        j+=1

    k = j+1
    while k <n:
        if l[k] != l[0]:
            c = min(c,((k-1)-j))
            j = k
            k = j+1
        else:
            k+=1

    if c == math.inf:
        print(-1)
    else:
        print(min(c,((k-1)-j)))
