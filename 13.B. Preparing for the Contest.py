t = int(input())
for _ in range(t):
    n,k = map(int,input().split())

    i = n-k
    while (i <=n):
        print(i)
        i+=1
    i = n-k-1
    while (i>=1):
        print(i)
        i-=1
     