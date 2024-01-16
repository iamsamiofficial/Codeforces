t = int(input())

for _ in range(t):
    n,f,a,b = map(int,input().split())
    m = list(map(int,input().split()))
    p = 0
    initial = 0
    for i in range(len(m)):
        c = min(((m[i]-initial)*a),b)
        if (f-c)<=0:
            p = 1
            break
        initial = m[i]
        f-=c
    if p:
        print("NO")
    else:
        print('YES')