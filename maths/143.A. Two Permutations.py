for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if n == a == b or a+b<n-1:
        print("YES")
        continue
    print("NO")