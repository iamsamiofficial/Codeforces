# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().split()))
#     odd = a.count(-1)
#     even = a.count(1)
#     c = 0
#     if odd&1:
#         odd-=1
#         even+=1
#         c+=1
#         if even>=odd:
#             print(c)
#         else:
#             while odd>even:
#                 c+=2
#                 odd-=2
#                 even+=2
#             print(c)
#     else:
#         if odd>even:
#             while odd>even:
#                 c+=2
#                 odd-=2
#                 even+=2
#             print(c)
#         else:
#             print(c)

for _ in range(int(input())):
    n = int(input())
    l = input()
    c = l.count("-1")
    x = max(c-n//2,0)
    print(x+(c-x)%2)
