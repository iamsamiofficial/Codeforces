
for _ in range(int(input())):
    x,y = map(int,input().split())
    ans = 0
    store = y%x
    s = y//x
        
    print((x-store)*s**2+(store)*(s+1)**2)