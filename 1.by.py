t = int(input())
for _ in range(t):
    n = int(input())
    a = [1]

    for i in range(1, n):
        a.append(a[i - 1] + 1)

    for i in range(n - 2):
        while (a[i] + a[i+1]) % (3 * a[i+2]) == 0 or a[i] >= a[i+1]:
            a[i+1] += 1
    print(*a)

