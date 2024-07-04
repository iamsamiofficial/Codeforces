
for _ in range(int(input())):
    inp = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0

    for i in range(inp):
        if a[i]>b[i]:
            a.append(b[i])
            a.sort()
            a.pop()
            c+=1
    print(c)