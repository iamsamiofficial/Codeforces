
for _ in range(int(input())):
    n,c,d = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    m = []
    p = l[0]
    k = 0
    for i in range(n):
        k = p
        for j in range(n):
            m.append(k)
            k+=c
            
        p +=d
        
    m.sort()
    if l == m:
        print("YES")
    else:
        print("NO")