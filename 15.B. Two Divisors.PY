t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    if n == 3:
        print(n*k)
    elif n>=2:
        print(k*2)
    else:
        print(k*k)