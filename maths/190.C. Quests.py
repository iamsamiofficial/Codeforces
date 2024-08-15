for _ in range(int(input())):
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    maxi = 0
    p = 0
    store = 0
    c = list(map(int,input().split()))
    d = 0
    for i in range(min(n,k)):
        d += b[i]
        p = max(p,c[i])
        maxi = max(maxi,d+(p*(k-(i+1))))
       
    print(maxi)


