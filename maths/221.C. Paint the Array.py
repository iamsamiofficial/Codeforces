# import math
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().split()))
#     i = 0
#     j = 1
#     ig = 0
#     jg = 0
#     while i<n:
#         ig = math.gcd(ig,a[i])
#         i+=2
#         if j<n:
#             jg = math.gcd(jg,a[j])
#         j+=2
#     i = 0
#     j = 1
#     while i <n:
#         if jg != 0 and a[i]%jg ==0:
#             jg = 0
#         if j<n and ig!=0 and a[j]%ig == 0:
#             ig = 0
#         i+=2
#         j+=2
#     if ig == 0 and jg == 0:
#         print(ig)
#     elif ig == 0:
#         print(jg)
#     else:
#         print(ig)

    
import math
for _ in range(int(input())):
    n = input()
    a = list(map(int,input().split()))
    even = a[0::2]
    odd = a[1::2]
    eg = math.gcd(*even)
    og = math.gcd(*odd)

    if all(e%og!=0 for e in even):
        print(og)
    elif all(o%eg != 0 for o in odd):
        print(eg)
    else:
        print(0)

