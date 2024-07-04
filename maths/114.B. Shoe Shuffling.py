for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if n == 1:
        print(-1)
        continue
    if l[0]!=l[-1]:
        print(-1)
        
    else:
        if n%2 == 0:
            ans = list(range(n,0,-1))
            print(*ans)
        else:
            ans = list(range(n,0,-1))
            j = (n//2)
            ans[0],ans[j] = ans[j],ans[0]
            print(*ans)