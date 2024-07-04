
for _ in range(int(input())):
    a,b = map(int,input().split())
    xk,yk = map(int,input().split())
    xq,yq = map(int,input().split())
    px = [a,a,-a,-a,b,b,-b,-b]
    py = [b,-b,b,-b,a,-a,a,-a]
    s1 = set()
    s2 = set()
    for i in range(len(px)):
        s1.add((xk+px[i],yk+py[i]))
        s2.add((xq+px[i],yq+py[i]))
    
    ans = s1.intersection(s2)
    print(len(ans))