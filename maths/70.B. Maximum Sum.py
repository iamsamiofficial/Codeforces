

for _ in range(int(input())):
    n,k = map(int,input().split())
    c = 0
    l = list(map(int,input().split()))
    p = 0
    if max(l)<=0:
        print(sum(l)%1000000007)
    
    else:
        i = 0
        while i < n:
            p+=l[i]
            if p<=0:
                p = 0
            else:
                c = max(p,c)
            i+=1
            
        ans = sum(l)
        ans+= c*(2**k-1)
        print(ans%1000000007)