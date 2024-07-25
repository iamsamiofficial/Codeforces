for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    for i in range(n-1):
        if l[i]%2 == l[i+1]%2:
            c+=1
    print(c)