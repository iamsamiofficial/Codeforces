for _ in range(int(input())):
    n = int(input())
    l = input().split()
    for i in range(1,n):
        tmp1 = l[:i]
        tmp2 = l[i:]
        mx1 = 0
        mx2 = 0
        c = 0
        while mx1 in tmp1:
            mx1+=1
        
        if mx1 in tmp2:
            continue
        else:
            tmp = list(set(tmp2))
            tmp = list(sorted(tmp))
            if tmp[:mx1] and tmp[mx1] < mx1:
                mx2 = mx1
                break

        if mx1 == mx2:
            c = 1
            p = 1
            q = i
            w = q+1
            x = n

            break
    
    if c == 1:
        print(2)
        print(p,q)
        print(w,x)
    else:
        print(-1)


