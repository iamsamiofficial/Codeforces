import math
for _ in range(int(input())):
    n,k,a,b = map(int,input().split())
    s = []
    mina = math.inf
    minb = math.inf
    for i in range(n):
        s.append(list(map(int,input().split())))
    t = abs(s[a-1][0]-s[b-1][0])+abs(s[a-1][1]-s[b-1][1])
    for i in range(k):
        mina = min(mina,abs(s[a-1][0]-s[i][0])+abs(s[a-1][1]-s[i][1]))
        minb = min(minb,abs(s[i][0]-s[b-1][0])+abs(s[i][1]-s[b-1][1]))
    print(min(t,mina+minb))
