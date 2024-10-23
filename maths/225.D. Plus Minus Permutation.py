import math
for _ in range(int(input())):
    n,x,y = map(int,input().split())
    l = (n//x)-(n//math.lcm(x,y))
    r = (n//y)-(n//math.lcm(x,y))
    ans = ((((n*(n+1))//2)-(((n-l)*(n-l+1))//2))-(r*(r+1))//2)
    print(ans)
    