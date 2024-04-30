t = int(input())

for _ in range(t):
    x,y,z = map(int,input().split())

    a1=b1 = x
    a2=c1 = y
    b2=c2 = z
    a = min(a1,a2)
    b = min(b1,b2)
    c = min(c1,c2)
    f = 0
    if max(a,b) == x and max(a,c) ==y and max(b,c) == z:
        print("YES")
        print(a,b,c)
    else:
        print("NO")