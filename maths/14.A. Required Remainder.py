t = int(input())

for _ in range(t):
    x,y,n = map(int,input().split())
    if y == 0:
        z = int(n/x)
    else:
        z = int(n/x)-1
    p = (z*x)+y
    print(p)