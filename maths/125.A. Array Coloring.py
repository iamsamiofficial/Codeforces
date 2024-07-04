for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    
    if sum(l)&1:
        print("NO")
    else:
        print("YES")
           