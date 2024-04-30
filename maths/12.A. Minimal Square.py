t = int(input())

for _ in range(t):
    x,y = map(int,input().split())

    z = min(x,y)
    z = 2*z
    print(max(x,y,z)*max(x,y,z))