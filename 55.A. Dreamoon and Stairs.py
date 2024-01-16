n,m = map(int,input().split())
c = 0
if n<m:
    print(-1)
else:
    if n%2 == 1:
        f= int((n+1)/2)
    else:
        f = int(n/2)
    while f<=n:
        if (f%m) == 0:
            c+=1
            break
        f+=1
    if c == 1:
        print(f)
    else:
        print(-1)

