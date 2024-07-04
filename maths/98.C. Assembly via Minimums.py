# # from collections import Counter
# # for _ in range(int(input())):
# #     n = int(input())
# #     b = list(map(int,input().split()))
# #     b.sort()
# #     ans = []
# #     p = 0
# #     i = 1
# #     while i < n:
# #         p = p+(n-i)
# #         ans.append(b[p-1])
# #         i+=1
# #     ans.append(ans[-1])
# #     print(*ans)

# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     l.sort()

#     # Precompute prefix sums
#     prefix_sums = [0] * (n + 1)
#     for i in range(1, n + 1):
#         prefix_sums[i] = prefix_sums[i - 1] + l[i - 1]

#     c = 0
#     for i in range(n):
#         if l[i] == prefix_sums[i]:
#             c += 1  # Found a valid subarray, no need to check further

#     print(c)




for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    pref = 0
    m = 0

    for i in l:
        pref+=i
        m = max(m,i)
        if m == pref-m:
            c+=1
    print(c)





