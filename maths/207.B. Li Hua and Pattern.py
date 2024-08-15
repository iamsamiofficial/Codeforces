for _ in range(int(input())):
    n,k = input().split()
    n = int(n)
    k = int(k)
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    
    t = 0
    b = n-1
    c = 0
    while t<=b:
        for i in range(len(p[0])):
            if p[t][i] != p[b][(n-1)-i]:
                p[t][i] = p[b][(n-1)-i]
                c+=1
        t+=1
        b-=1
    if c>k:
        print("NO")
        continue
    if k>c:
        if(k-c)%2 == 0:
            print("YES")
        else:
            if n&1:
                print("YES")
            else:
                print("NO")
        continue
    print("YES")
