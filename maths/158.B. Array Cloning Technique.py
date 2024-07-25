from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = input().split()
    d = Counter(a)
    maxi = max(d.values())
    c = n-maxi
    while maxi<n:
        c+=1
        maxi *= 2
    print(c)
    
    # ans = 0
    
    # while maxi<n:
    #     c+=1
    #     if maxi<=(n-maxi):
    #         ans+=maxi
    #     else:
    #         ans += (n-maxi)
    #     maxi+=maxi #0 1 3 3 7 0
        
    # print(c+ans)
   