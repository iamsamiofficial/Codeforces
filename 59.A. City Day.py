x,y,z = map(int,input().split())
l = list(map(int,input().split()))
c = 0
mini = 9999999999999999999999999

for i in range(x):
    mini = min(l[i-y:i]) if l[i-y:i] else 99999999999999999999999999999
    c = min(l[i+1:i+z+1]) if l[i+1:i+z+1] else 9999999999999999999999999

    if mini >l[i] and c >l[i]:
        break
print(i+1)
