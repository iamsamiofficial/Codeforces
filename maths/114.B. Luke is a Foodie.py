

for _ in range(int(input())):
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    maxi = l[0]+x
    mini = abs(l[0]-x)
    c = 0
    for i in range(1,n):
        mini = max(0,l[i]-x)

        if maxi>= mini:
            mini = max(0,l[i]-x)
            maxi = l[i]+x
        else:
            mini = max(0,l[i]-x)
            maxi = l[i]+x
            c+=1
    print(c)
