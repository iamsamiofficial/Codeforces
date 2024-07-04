for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = l.count(2)
    
    if c == 0:
        print(1)
    elif c&1:
        print(-1)
    else:
        c = c//2
        i = 0
        while c>0:
            if l[i] == 2:
                c-=1
                ans = i
            i+=1
        print(ans+1)