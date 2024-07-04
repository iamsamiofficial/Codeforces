
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    seen = set()
    c = 0
    
    for i in range(n):
        seen.add(s[i])
        c += len(seen)
        
    print(c)
