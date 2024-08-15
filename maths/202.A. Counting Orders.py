mod = 10**9+7
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b.sort()
    c.sort()
    res = []
    j = 0
    for i in range(n):
        while j<n:
            if b[j]>c[i]:
                res.append(n-j)
                break
            j+=1
    
    if len(res)==n:
        res.sort()
        ans = 1
        for i in range(len(res)):
            ans= ((ans%mod)*((res[i]-i)%mod)%mod)
        print(ans)

        continue
    print(0)