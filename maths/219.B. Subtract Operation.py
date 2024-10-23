for _ in range(int(input())):
    n,k = input().split()
    n = int(n)
    k = int(k)
    l = list(map(int,input().split()))
    l = set(l)
    for i in l:
        if i+k in l:
            print("YES")
            break
    else:
        print("NO")