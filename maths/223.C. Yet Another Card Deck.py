n,q = map(int,input().split())
a = list(map(int,input().split()))
t = list(map(int,input().split()))
ans = []
# for i in t:
#     ind = a.index(i)
#     ans.append(ind+1)
#     a[:ind+1] = [i]+a[:ind]
for i in t:
    ind = a.index(i)
    ans.append(ind+1)
    p = a.pop(ind)
    a = [p]+a
print(*ans)