for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    i = 1
    while i<n:
        if a[i-1] == 1:
            a[i-1] = 2
        if a[i] == 1:
            a[i] = 2
        if a[i]%a[i-1] == 0:
            a[i] = a[i]+1
        i+=1
    print(*a)
    