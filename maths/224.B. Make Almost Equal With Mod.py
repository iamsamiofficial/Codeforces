for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 2
    d = set()
    c = 0
    while True:
        for j in range(n):
            d.add(l[j]%ans)
            if len(set(d)) == 2:
                c=1
                break  
        if c == 1:
            break
        d = set()
        ans*=2
    print(ans)
