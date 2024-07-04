for _ in range(int(input())):
    n,x = map(int,input().split())
    l = [0]+list(map(int,input().split()))
    ans = 2*(x-l[-1])
    for i in range(1,len(l)):
        ans = max(ans,l[i]-l[i-1])
        
    print(ans)
