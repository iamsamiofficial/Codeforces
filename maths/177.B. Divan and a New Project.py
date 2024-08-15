for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = [i//2 if i%2 == 0 else -((i//2)+1) for i in range(1,n+1)]
    s = 0
    l = sorted(enumerate(l),key=lambda x:x[1],reverse=True)
    #print(l)
    co = [0]*n
    #print(co)
    for i in range(n):
        s+=l[i][1]*(2*(abs(ans[i])))
        co[l[i][0]] = ans[i]
    print(s)
    print(*([0]+co))