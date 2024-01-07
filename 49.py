n,m = map(int,input().split())
c = 0
if m%n == 0:
    result = m//n
    while result %2 == 0:
        result //=2
        c+=1
    while result %3 == 0:
        result //=3
        c+=1
    if result == 1:
        print(c)
    else:
        print(-1)
else:
    print(-1)