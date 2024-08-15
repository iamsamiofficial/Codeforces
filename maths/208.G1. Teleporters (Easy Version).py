for _ in range(int(input())):
    n,c = input().split()
    n = int(n)
    c = int(c)
    b = list(map(int,input().split()))
    for i in range(n):
        b[i] = b[i]+i+1
    b.sort()
    d = 0
    for i in b:
        c-=i
        if c>=0:
            d+=1
        else:
            break
    print(d)