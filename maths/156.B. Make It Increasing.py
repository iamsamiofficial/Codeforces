for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    c = 0
    for i in range(n-1,0,-1):
        while a[i]<= a[i-1] and a[i-1]!= 0:
            a[i-1]= a[i-1]//2
            ans+=1
        if a[i-1] == a[i]:
            c = 1
            break
    if c == 1:
        print(-1)
    else:
        print(ans)

