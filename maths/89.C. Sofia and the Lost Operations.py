from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = input().split()
    b = input().split()
    m = int(input())
    d = input().split()
    p = Counter(b[i] for i in range(n) if a[i]!=b[i])

    for i in d:
        if i in p:
            p[i]-=1
            if p[i]==0:
                del p[i]

    if p or i not in b:
        print("NO")
    else:
        print("YES")

        
