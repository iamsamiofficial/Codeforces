for _ in range(int(input())):
    x,y,z = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    l3 = []
    l4 = []

    for i in l1:
        if i>0 and i<=z:
            l3.append(i)
    for i in l2:
        if i>0 and i<=z:
            l4.append(i)
    s = list(set(l3))
    t = list(set(l4))
    if len(s)>= z//2 and len(t)>= z//2:
        l5 = l3+l4
        if len(set(l5)) == z:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

