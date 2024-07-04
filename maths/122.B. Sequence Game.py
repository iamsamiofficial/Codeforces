for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = []
    c = 0
    for i in range(1,n):
        if l[i]<l[i-1]:
            c = 1
            n+=1
            m.append(l[i-1])
            m.append(1)
        else:    
            m.append(l[i-1])
    
    print(n)
    if c  == 1:
        m.append(l[-1])
        print(*m)
    else:
        print(*l)

