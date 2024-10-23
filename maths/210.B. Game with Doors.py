for _ in range(int(input())):
    c,d = map(int,input().split())
    e,f = map(int,input().split())
    t = max(c,e)
    y = min(d,f)
    ns = 0
    if t<=y:
        ns = y-t
    if t>y:
        ns+=1
        print(ns)
        continue
    if min(c,e)<t:
        ns+=1
    if max(d,f)>y:
        ns+=1
    print(ns)
