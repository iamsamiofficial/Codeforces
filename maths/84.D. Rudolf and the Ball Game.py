for _ in range(int(input())):
    n,m,x = map(int,input().split())
    ans = set([x])
    for _ in range(m):
        y,z = input().split()
        y = int(y)
        tmp = set()
        if z == "?":
            for i in ans:
                if i+y <= n:
                    tmp.add(i+y)
                elif (i+y)>n:
                    tmp.add((i+y)-n)
                if (i-y) >0:
                    tmp.add(i-y)
                elif (i-y)<=0:
                    tmp.add((n-abs(i-y)))
        elif z == "1":
            for i in ans:
                if (i-y) >0:
                    tmp.add(i-y)
                elif (i-y)<=0:
                    tmp.add((n-abs(i-y)))
        elif z == "0":
            for i in ans:
                if i+y <= n:
                    tmp.add(i+y)
                elif (i+y)>n:
                    tmp.add((i+y)-n)
            
        ans = tmp

    print(len(ans))
    print(*(sorted(ans)))


