t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    c = 0
    final = 0
    p = 0
    l = 0
    r = 0
    i = 0
    j = n-1
    le = 0
    ri = 0
    while i <=j:
        if s[i] == "1":
            le = 1
            break
        elif s[j] == "1":
            ri = 1
            break
        i+=1
        j-=1
        l+=1
        r+=1
    if le == 1:
        final = n-l
        
    else:
        final = n-r
    final = 2*final
    if le == 0 and ri == 0:

        print(n)
    else:
        print(final)
        
