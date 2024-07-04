for _ in range(int(input())):
    n  = int(input())
    ans = []
    a = list(map(int,input().split()))
    mex = n
    for i in a[::-1]:
        ans.append(mex-i)
        mex = min(mex,mex-i)
    print(*ans[::-1])