n,x = map(int,input().split())
d = list(map(int,input().split()))
b = list(map(int,input().split()))


for i in b:
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if d[mid] == i:
            break
        elif d[mid] >i:
            r = mid-1
        else:
            l = mid+1
    if d[mid] == i:
        print("YES")
        continue
    print("NO")