t = int(input())

for _ in range(t):
    n = int(input())#9876 #9870
    x = 1
    arr = []
    while n:
        x*=10
        p = n%x
        if p:
            arr.append(p)
        n = n-p
    print(len(arr))
    print(" ".join(map(str,arr)))

