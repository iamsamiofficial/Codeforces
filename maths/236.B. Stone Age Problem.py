n,q = map(int,input().split())
a = list(map(int,input().split()))
d ={}
s = 0
for i in range(len(a)):
    d[i+1] = a[i]
    s+=a[i]
c = 0
for i in range(q):
    p = list(map(int,input().split()))
    if len(p) == 2:
        d.clear()
        s = n*p[1]
        d[-1] =p[1]
    else:
        if (p[1]) in d:
            s = s+ (p[2]-d[p[1]])
        else:
            s = s+(p[2]-d[-1])
        d[p[1]] = p[2]
    print(s)
            
