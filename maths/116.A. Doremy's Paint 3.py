from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    f = Counter(l)
    if len(f)>2:
        print("NO")
        continue
    a = []
    for i,j in f.items():
        a.append(j)
    
    if (a[0] == n or a[1] == n or abs(a[0]-a[1]) == 1 or abs(a[0]-a[1]) == 0):
        print("YES")
        continue
        
    print("NO")

