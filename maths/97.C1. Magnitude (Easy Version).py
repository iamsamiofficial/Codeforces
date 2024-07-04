# n = int(1e6 + 5)
# mod = 998244353

# for _ in range(int(input())):
#     n = int(input())
#     a = [0]+list(map(int, input().split()))
#     a1 = [0]*(n+1)
#     a2 = [0]*(n+1)
#     w1 = [0]*(n+1)
#     w2 = [0]*(n+1)
#     a1[1] = max(a[1],abs(a[1]))
#     a2[1] = min(a[1],abs(a[1]))

#     if a[1]>=0:
#         w1[1] = 2
#         w2[1] = 2
#     else:
#         w1[1] = 1
#         w2 [1] = 1
    
#     for i in range(2,n+1):
#         a1[i] = max(a1[i-1]+a[i],abs(a1[i-1]+a[i]),a2[i-1]+a[i],abs(a2[i-1]+a[i]))

#         if a1[i] == a1[i-1]+a[i]:
#             w1[i] = (w1[i]+w1[i-1])%mod
#         if a1[i] == abs(a1[i-1]+a[i]):
#             w1[i] = (w1[i]+w1[i-1])%mod

#         if a1[i-1]!=a2[i-1]:
#             if a1[i]==a2[i-1]+a[i]:
#                 w1[i] = (w1[i]+w2[i-1])%mod
#             if a1[i]==abs(a2[i-1]+a[i]):
#                 w1[i] = (w1[i]+w2[i-1])%mod

#         a2[i] = min(a1[i-1]+a[i],abs(a1[i-1]+a[i]),a2[i-1]+a[i],abs(a2[i-1]+a[i]))

#         if a2[i] == a1[i-1]+a[i]:
#             w2[i] = (w2[i]+w1[i-1])%mod
#         if a2[i] == abs(a1[i-1]+a[i]):
#             w2[i] = (w2[i]+w1[i-1])%mod

#         if a1[i-1]!=a2[i-1]:
#             if a2[i]==a2[i-1]+a[i]:
#                 w2[i] = (w2[i]+w2[i-1])%mod
#             if a2[i]==abs(a2[i-1]+a[i]):
#                 w2[i] = (w2[i]+w2[i-1])%mod

#         print(w1[n])
#         for i in range(1,n+1):
#             w1[i]=w2[i]=0

        
for _ in range(int(input())):
    n = int(input())
    a = [0]+list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    dpp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if a[i] > 0:
            dpp[i] = dp[i - 1] + a[i]
            dp[i] = max(dp[i - 1] + a[i], abs(dpp[i - 1] + a[i]))
        else:
            dpp[i] = dpp[i - 1] + a[i]
            dp[i] = max(dp[i - 1] + a[i], abs(dpp[i - 1] + a[i]))
            
    print(dp[n])

