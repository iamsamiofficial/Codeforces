for _ in range(int(input())):
    n,k = input().split()
    n = int(n)
    k = int(k)
    s = input()
    w = 0
    pre = [0]
    for i in range(n):
        if s[i] == "W":
            pre.append(pre[-1]+1)
        else:
            pre.append(pre[-1])
    ans = pre[k]
    i = k+1
    while i <= n:
        ans = min(ans,pre[i]-pre[i-k])
        i+=1
    print(ans)
    #print(pre)
    # for i in range(k):
    #     if s[i] == "W":
    #         w+=1
    # ans = w

    # i = 0
    # while i+k <n:
    #     if s[i] == "W":
    #         w-=1
    #     if s[i+k] == 'W':
    #         w+=1
    #     ans = min(ans,w)
    #     i+=1
    # print(ans)
    