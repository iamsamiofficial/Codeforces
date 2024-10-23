from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    p = Counter(l)
    
    ans = 0
    for i in set(l):
        if p[i]>p[i-1]:
            ans+= p[i]-p[i-1]
    print(ans)
            


    
    
