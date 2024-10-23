for _ in range(int(input())):
    n,m = map(int,input().split())
    l = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(m):
        l1 = [l[j][i] for j in range(n)]
        l1.sort()
        k = [0]
        for i in l1:
            k.append(k[-1]+i)
        for j in range(n-1):
            ans+= (k[-1]-k[j+1])-(l1[j]*(n-(j+1)))
    print(ans)

    
    # l = list(map(int,input().split()))
    # ans = 0
    # for i in range(n-1):
    #     j = list(map(int,input().split()))
    #     p = 0
    #     while p<len(l):
    #         ans+=abs(j[p%len(j)]-l[p%len(l)])
    #         p+=1
    #     l = l+j
    # print(ans)