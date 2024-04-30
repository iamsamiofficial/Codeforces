t = int(input())

for _ in range(t):
    x,y = map(int,input().split())
    
    c = abs(x-y)+9

    ans = (c/10)
    print(int(ans))
