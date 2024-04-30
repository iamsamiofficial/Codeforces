t = int(input())

# for i in range(t):
#     n = int(input())
#     l = list(map(int,input().split()))
#     c = 0
#     k = 0
#     for i in range(n):
#         if i%2 == 0:
#             if l[i]%2 == 1:
#                 j = i+1
#                 while j<n:
#                     if l[j]%2 == 0:
#                         l[i],l[j] = l[j],l[i]
#                         c+=1
#                         break
#                     j+=2
#         elif i%2 == 1:
#             if l[i]%2 == 0:
#                 j = i+1
#                 while j <n:
#                     if l[j]%2 == 1:
#                         l[i],l[j] = l[j],l[i]
#                         c+=1
#                         break
#                     j+=2
    
#     for i in range(n):
#         if ((i%2 == 0 and l[i]%2 == 1) or (i%2==1 and l[i]%2 == 0)):
#             k = 1
#             break
#     if k == 1:
#         print(-1)
#     else:
#         print(c)

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    a = b = 0
    for i in range(len(l)):
        if l[i] %2 != i%2:
            if i%2 == 0:
                a+=1
            else:
                b+=1
    if a==b:
        print(a)
    else:
        print(-1)

        