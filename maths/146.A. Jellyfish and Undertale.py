for _ in range(int(input())):
    a,b,n = map(int,input().split())
    l = list(map(int,input().split()))
    ans = b
    for i in l:
        ans+= min(a-1,i)
    print(ans)