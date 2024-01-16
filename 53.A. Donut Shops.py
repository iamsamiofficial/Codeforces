t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())
    if a>c:
        print(-1,b)
    elif a<c and (a*b) <= c:
        print(1,-1)
    elif a<c and (a*b)> c:
        print(1,b)
    elif a==c and b == 1:
        print(-1,-1)
    elif a == c and (a*b)>c:
        print(-1,b)
    
    
