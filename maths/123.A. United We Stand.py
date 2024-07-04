
# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     l.sort()
#     if l[0] == l[-1]:
#         print(-1)
#         continue
#     b = []
#     c = [l[-1]]
#     for i in range(len(l)-2,-1,-1):
#         if l[i] == c[-1]:
#             c.append(l[i])
#         else:
#             b = l[:i+1]
#             break
#     print(len(b),len(c))
#     print(*b)
#     print(*c)


for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    if l[0] == l[-1]:
        print(-1)
        continue
    k = l.count(l[-1])
    print(n-k,k)
    print(*l[:n-k])
    print(*l[n-k:])
