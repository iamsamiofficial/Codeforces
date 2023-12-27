n = int(input())
l = 0
r = 0
for i in range(n):
    k,m = input().split()
    k = int(k)
    m = int(m)
    if k == 0:
        l+=1
    if m == 0:
        r+=1

if (n-l) < l:
    l1 = (n-l)
else:
    l1 = l
if (n-r) < r:
    r1 = (n-r)
else:
    r1 = r
print(l1+r1)

