t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    sl = 99999999
    tl = 99999999
    p = 0
    for i in range(n):
        
        if sl>tl:
            x = tl
            tl = sl
            sl = x
        if l[i] <=sl:
            sl = l[i]
        elif l[i] <=tl:
            tl = l[i]
        else:
            sl = l[i]
            p+=1
    print(p)
        