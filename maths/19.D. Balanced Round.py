for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 1
    c = 1
    for i in range(1,n):
        if a[i]-a[i-1]>k:
            c = 1
        else:
            c+=1
            ans = max(c,ans) #2 3 8 10 19
    print(n-ans)
    
