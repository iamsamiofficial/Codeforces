
results = []
    
for _ in range(int(input())):
    n,m = map(int,input().split())
        
    if m > n:
         results.append("NO")
    else:
        if (n - m) % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    
for result in results:
    print(result)

