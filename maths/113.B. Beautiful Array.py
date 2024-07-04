import math
for _ in range(int(input())):
    n,k,b,s = map(int,input().split())
    p = min(s,(k*b)+(k-1))
    l = []
        
        
    if k*b>s or s-p>(n-1)*(k-1):
        print(-1)
    
    else:
        a = s-p
        for i in range(n-1):
            l.append(a//(n-1))
        for i in range(a%(n-1)):
            l[i]+=1
        l.append(p)
        print(*l)

