for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    k = list(map(int,input().split()))
    p = list(enumerate(k))
    p.sort(key=lambda x:x[1])
    ans = [-1]*q
    pre = [0]
    for i in a:
        pre.append(pre[-1]+i)
    i = 0
    j = 0
    while i<q:
        while j<n:
            if p[i][1]<a[j]:
                ans[p[i][0]] = pre[j]
                break
            j+=1
        if j == n:
            break
        i+=1
    while i<q:
        ans[p[i][0]]=pre[-1]
        i+=1
    print(*ans)

