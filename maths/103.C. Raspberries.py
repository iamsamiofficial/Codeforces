import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    ans = math.inf
    c = 0
    if math.prod(l)%k == 0:
        print(0)
    else:
        for i in l:
            ans = min(ans,(k-(i%k)))
            if k == 4 and (k-(i%k)) == 2:
                c+=1
        if ans == 3 and k == 4:
            print(2)
        elif k == 4 and c==1:
            print(1)
        else:
            print(ans)
