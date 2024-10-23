for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    le = 0
    re = 0
    mini = 1
    maxi = n
    l = 0
    r = n-1
    while l<=r:
        if li[l] == mini:
            mini+=1
            l+=1
        elif li[r] == mini:
            mini+=1
            r-=1
        elif li[l] == maxi :
            maxi-=1
            l+=1
        elif li[r] == maxi:
            maxi-=1
            r-=1
        else:
            le = 1
            break
    if le == 1:
        print(l+1,r+1)
        continue
    print(-1)
    