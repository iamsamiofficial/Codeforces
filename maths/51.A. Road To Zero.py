
for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    ans = 0
    if (x<=0 and y>=0) or (x>=0 and y<=0):
        ans = (abs(x)*a) + (abs(y)*a)
    else:
        if 2*a <b:
            ans = (abs(x)*a)+(abs(y)*a)
        else:
            j = min(x,y)
            f = j * b
            k = max(x,y)
            l = k-j
            ans = f+(l*a)
    print(ans)
