

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    l = sorted(list((arr)))
    k = []
    c = 1
    for i in l:
        if i%l[0]:
            k.append(i)

    if k:
        for j in k:
            if j%k[0]:
                c = 0
                break
 
    
    if c == 1:
        print("YES")
    else:
        print("NO")



