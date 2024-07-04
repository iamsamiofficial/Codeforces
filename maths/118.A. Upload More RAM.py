# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     a = []
#     c = 0
#     p = 0
#     if l == sorted(l):
#         print(c)
#         continue
#     for i in range(1,n):
#         if l[i]<l[i-1]:
#             a.append(l[i-1]-l[i])
#             l[i]+=(l[i-1]-l[i])
#     a.sort()
#     j = len(a)+1
#     for i in a:
#         l = i-p
#         p+= (i-p)
#         c+=(l*j)
#         j-=1
#     print(c)


for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    ans = l[-1]

    for i in range(len(l)-2,-1,-1):
        ans = max(l[i],ans+1)
    print(ans)
