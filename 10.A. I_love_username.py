n = int(input())
x = list(map(int,input().split()))
a = 0
best = x[0]
worst = x[0]
i = 1
while i <n:
    if x[i] > best:
        a+=1
        best = x[i]
    if x[i] < worst:
        a+=1
        worst = x[i]
    i+=1
print(a)