for _ in range(int(input())):
    s,t = input().upper().split()
    d = 0
    for i in s[::-1]:
        if i == t[-1]:
            t = t[:-1]
        elif i in t:
            d = 1
            break
        if not t:
            break
    if  t or d:
        print("NO")
        continue
    print("YES")    # ans = []
    # j = len(t)-1
    # c = 0
    # d = 0
    # for i in range(len(s)-1,-1,-1):
    #     if j>=0:
    #         if s[i] == t[j]:
    #             if t[j] in ans:
    #                 d = 1
    #                 break
    #             j-=1
    #             c+=1
    #         else:
    #             ans.append(s[i])
                
    #     else:
    #         break
    # if c!= len(t) or d == 1:
    #     print("NO")
    # else:
    #     print("YES")
