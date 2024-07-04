for _ in range(int(input())):

    n = int(input())
    l = input().upper()
    c = 0
    for i in l:
        if i == "U":
            c+=1
    if c%2 == 0:
        print("NO")
    else:
        print("YES")

