d = [0]
for i in range(1,31):
    d.append(2**i)

for _ in range(int(input())):
    n,q = map(int,input().split())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    mn = c[0]
    for i in range(len(c)):
        if i> 0 and c[i]>= mn:
            continue
        mn = c[i]
        for j in range(len(b)):
            if b[j]%d[c[i]] == 0:
                b[j]+= d[c[i]]//2
    print(*b)
