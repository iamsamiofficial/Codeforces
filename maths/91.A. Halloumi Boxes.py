for _ in range(int(input())):
    p,k = map(int,input().split())
    n = list(map(int,input().split()))
    if n != sorted(n) and k==1:
        print("NO")
    else:
        print("YES")