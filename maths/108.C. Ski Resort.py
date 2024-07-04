for _ in range(int(input())):
    n,k,q = map(int,input().split())
    c = 0
    ans = 0
    l = list(map(int,input().split()))

    i = 0
    j = k
    while j<=n:
        if max(l[i:j])>q:
            ans += (c*(c+1))//2
            c=0
        else:
            c+=1
        i+=1
        j+=1
    ans += (c*(c+1))//2

    print(ans)