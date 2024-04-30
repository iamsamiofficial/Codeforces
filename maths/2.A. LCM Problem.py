t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    x = a
    y = 2*a
    if y<=b:
        print(x,y)
    else:
        print(-1,-1)