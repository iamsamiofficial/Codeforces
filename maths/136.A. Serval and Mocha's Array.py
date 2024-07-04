import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    up = 0
    down = 0
    for i in range(1,n):
        if math.gcd(l[i-1],l[i])>2:
            up+=1
        else:
            down+=1

    if up>down:
        print("NO")
    else:
        print("YES")