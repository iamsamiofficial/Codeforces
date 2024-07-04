# for _ in range(int(input())):
#     n,c = input().split()
#     s = input()
#     ans = 0
#     if c == "g":
#         print(0)
#         continue
#     for i in range(int(n)):
#         p = 0
#         if s[i] == c:
#             j = i+1
#             if j==int(n):
#                 j = 0
#             while s[j]!="g":
#                 p+=1
#                 j+=1
#                 if j == int(n):
#                     j = 0
#             p+=1
#             ans = max(ans,p)            
#     print(ans)

for _ in range(int(input())):
    n,c = input().split()
    n = int(n)
    s = input()
    
    if s[-1] == "g":
        s = s
    else:
        m = ""
        for i in s:
            if i == "g":
                m+=i
                break
            else:
                m+=i
        s = s+m
    p = len(s)
    ans = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == "g":
            p = i
        if s[i] == c:
            ans = max(ans,p-i)
    print(ans)