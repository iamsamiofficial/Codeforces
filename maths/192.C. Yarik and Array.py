for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    c= b[0]
    mxi =c
    for i in range(1,n):
        if c<0 or (b[i-1]%2 == b[i]%2):
            c = 0

        c+=b[i]
        mxi = max(mxi,c)
    print(mxi)

