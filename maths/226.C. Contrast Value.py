for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 1
    k = -1
    for i in range(1,n):
        if l[i]> l[i-1]:
            if k !=1:
                ans+=1
            k = 1
        elif l[i]<l[i-1]:
            if k!=0:
                ans+=1
            k = 0
    print(ans)