for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(input())
    c = 0
    if arr[0][0] == arr[-1][-1] or arr[0][-1] == arr[-1][0]:
        print("YES")
    else:
        for i in range(m):
            if arr[0][i] == arr[-1][-1]:
                for j in range(n):
                    if arr[j][0] == arr[-1][-1]:
                        c = 1
                        break
                if c==1:
                    break
        if c == 0:
            for i in range(m):
                if arr[0][i] == arr[-1][0]:
                    for j in range(n):
                        if arr[j][-1] == arr[-1][0]:
                            c = 1
                            break
                    if c==1:
                        break
        if c == 0:
            for i in range(m):
                if arr[0][0] == arr[-1][i]:
                    for j in range(n):
                        if arr[j][-1] == arr[0][0]:
                            c = 1
                            break
                    if c==1:
                        break
        if c == 0:
            for i in range(m):
                if arr[0][-1] == arr[-1][i]:
                    for j in range(n):
                        if arr[j][0] == arr[0][-1]:
                            c = 1
                            break
                    if c==1:
                        break
        
        if c == 1:
            print("YES")
        else:
            print("NO")
