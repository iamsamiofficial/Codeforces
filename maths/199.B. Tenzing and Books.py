for _ in range(int(input())):
    n,x = map(int,input().split())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    ns = 0
    for i in b:
        if i|x != x:
            break
        ns = ns|i
    if ns == x:
        print("YES")
        continue
    
    for i in c:
        if i|x != x:
            break
        ns = ns|i
    if ns == x:
        print("YES")
        continue
    for i in d:
        
        if i|x != x:
            break
        ns = ns|i
    if ns == x:
        print("YES")
        continue
    print("NO")