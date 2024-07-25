# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int,input().split()))
#     ans = []
#     s = 0
#     d = 0
#     for i in a:
#         if i != 0:
#             s+=1
#         else:
#             if s>0:
#                 ans.append(s)
#                 if len(ans)> 1:
#                     d = 1
#                     break
#             s = 0
#     if s>0:
#         ans.append(s)
#     if d == 1:
#         print(2)
#     else:
#         print(len(ans))
print(input().split("0"))