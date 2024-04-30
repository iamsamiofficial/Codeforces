t = int(input())

for _ in range(t):
    n = int(input())

    if (int(n/2)%2 == 1):
        print("NO")
    else:
        arr = []
        i = 2
        while i<=n:
            arr.append(i)
            i+=2
        i = 1
        while i<n-1:
            arr.append(i)
            i+=2

        arr.append((n-1)+int(n/2))
        print("YES")
        print(*arr,sep=" ")