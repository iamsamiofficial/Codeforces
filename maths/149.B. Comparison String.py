import math
for _ in range(int(input())):
   
    n = int(input())
    s = input()
    maxi = 2
    ans = 2
    for i in range(1,n):
        if s[i]==s[i-1]:
            ans+=1
            maxi = max(maxi,ans)
        else:
            ans = 2
    print(maxi)#>><>><>