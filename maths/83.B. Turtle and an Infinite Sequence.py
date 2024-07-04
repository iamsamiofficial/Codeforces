for _ in range(int(input())):
    n,m = map(int,input().split())
    l = max(0,n-m)
    r = n+m

    x = (l^r).bit_length()
    print(l|r|(1<<x)-1)
    