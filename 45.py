t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    indice = []
    s = [l[0]] if l else None
    t = []
    for i in range(1,n):
        if l[i]<= l[i-1]:
            indice.append(i)
            s.append(l[i])
        else:
            continue
