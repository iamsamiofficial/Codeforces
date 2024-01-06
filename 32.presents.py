n = int (input())
l = list(map(int,input().split()))
arr = []
for i in range(1,n+1):
    for j in range(n):
        if l[j] == i:
            arr.append(j+1)
print(" ".join(map(str,arr)))

