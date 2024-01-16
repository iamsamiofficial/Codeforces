n,k = map(int,input().split())
m = list(map(int,input().split()))

p = sorted(m)
i = 0
c = 0
final = []
while i<len(p) and k-p[i]>=0:
    k-=p[i]
    i+=1

for j in range(i):
    k = 0
    while k <len(p):
        if p[j] == m[k] and (k+1) not in final:
            final.append(k+1)
            break
        k+=1

print(i)
print(*final)




