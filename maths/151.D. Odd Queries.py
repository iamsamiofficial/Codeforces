for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    j = [0]+[a[0]]
    for i in range(1,n):
        j.append(j[-1]+a[i])
    for i in range(q):
        l,r,k = map(int,input().split())
        ans = (j[l-1])+((r-l+1)*k)+(j[-1]-j[r])

        if ans&1:
            print("YES")
        else:
            print("NO")