t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int,input()))
    f = list(map(int,input()))
    c = 0
    cn = 0
    cn1 = 0
    for i in range(n):
        if f[i] == 1:
            cn+=1
        if s[i] == 1:
            cn1+=1
        
        if s[i] != f[i] and f[i] == 1:
            c+=1
    
    if cn1>cn:
        c+=(cn1-cn)
    print(c)
    # final = 0
    # for i in range(n):
    #     c = 0
    #     if s[i] == f[i]:
    #         continue

    #     else:
    #         j = i+1
    #         while j<n:
    #             if s[i] == f[j] and s[j] == f[i]:
    #                 s[i],s[j] = s[j],s[i]
    #                 break
    #             else:
    #                 j+=1
    #         final+=1
            
    # print(final)




