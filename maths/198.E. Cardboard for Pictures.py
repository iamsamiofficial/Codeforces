for _ in range(int(input())):
    n,c = input().split()
    p = list(map(int,input().split()))
    #p.sort(reverse=True)
    n = int(n)
    c = int(c)
    r = 10**9
    l = 0
    while l<=r:
        ns = 0
        mid = (l+r)//2
        for i in p:
            ns+= (2*mid+i)**2
            if ns>c:
                break
        if ns == c:
            break
        elif ns>c:
            r = mid-1
        else:
            l = mid+1
    print(mid)