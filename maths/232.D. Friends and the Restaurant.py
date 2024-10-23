for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    p = []     
    for i in range(n):
        p.append(y[i]-x[i])
    p.sort()
    c = 0
    i = 0
    j = n-1
    while i<j:
        if p[j]+p[i]>=0:
            c+=1
            i+=1
            j-=1
        else:
            i+=1
    print(c)
