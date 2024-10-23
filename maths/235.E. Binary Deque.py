for _ in range(int(input())):
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    p = sum(a)
    if s>p:
        print(-1)
        continue
    elif s==p:
        print(0)
        continue
    d =[0]
    for i in range(n):
        if a[i] == 1:
            d.append(i+1)
    d.append(n+1)
    p = 1
    c = 99999999999999999999999
    for i in range(s,len(d)-1):
        c = min(c,(d[p-1])+((n-d[i+1])+1))
        p+=1
    print(c)
    

