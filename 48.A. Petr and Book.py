n = int(input())

l = list(map(int,input().split()))
sum = 0
c = 0

while sum <n:
    for i in range(len(l)):
        if sum<n:
            sum+=l[i]
            c = i+1
        else:
            break
print(c)
