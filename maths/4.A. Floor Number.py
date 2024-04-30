t = int(input())

for _ in range(t):
    n,x = map(int,input().split())

    
    n-=2
    if n>0:
        if n%x == 0:
            print((n//x)+1)
        else:
            print((n//x)+2)
    else:
        print(1)


