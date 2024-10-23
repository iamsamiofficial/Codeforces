for _ in range(int(input())):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    ans=[(l[0]-1)+(n-(l[-1]))]
    if ans[0]<0:
        ans[0] = 0
    for i in range(1,m):
        ans.append(l[i]-(l[i-1]+1))
    ans.sort(reverse=True)
    p = m
    j = 1
    for i in ans:
        if j>i:
            p+=i
        elif j == i:
            p+=(j-1)
        else:
            p+=j
        j+=4
    print(p)
    #5+1+5+9+9
