t = int(input())

for _ in range(t):
    a,b,c,n = map(int,input().split())
    z = max(a,b,c)
    x = z-a
    y = z-b
    z = z-c
    n = n-(x+y+z)
    if n>=0 and n%3 ==0:
        print("YES")
    else:
        print("NO")
