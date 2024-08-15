import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    q = b
    p = a
    c = 0
    
    if q == 1:
        c+=1
        q+=1
    ans = [math.inf]
    while q<a:
        p = a
        while p>0:
            p=p//2
            c+=1
        if c>ans[-1]:
            break
        ans.append(c)
        q+=1
        c = q-b
    print(min(ans))

    # while p>0:
    #     p=p//q
    #     c+=1
    
    # ans.append(c)
    # q+=1
    # c = abs(b-q)
    # while q<a:
    #     p = a
    #     while p>0:
    #         p = p//q
    #         c+=1
    #     if c>ans[-1]:
    #         break
    #     ans.append(c)
    #     q+=1
    #     c = abs(b-q)
    # print(min(ans))        
    
