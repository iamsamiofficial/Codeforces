x,y = map(int,input().split())
arr = []
for i in range (x):
    arr.append(int(input()))

dic = {}

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1
ans = 0
for key,value in dic.items():
    if value%2 == 0:
        ans+=value
    else:
        ans+=(value-1)

import math
c = math.ceil(x/2)
jack = math.ceil(ans/2)

if jack<c:
    ans+=(c-jack)
print(ans)