t = int(input())
for _ in range(t):
    x,y,n = map(int,input().split())
    k = int(n/x)
    j = (x*k)+y
    if j>n:
        k = int(n/x)-1
        j = (x*k)+y
        print(j)
    else:
        print(j)