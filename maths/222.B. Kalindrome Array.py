for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    j = n-1
    le = 0
    ri = 0
    c = 1
    while i<j:
        if a[i] == a[j]:
            i+=1
            j-=1
        else:
            le = a[i]
            ri = a[j]
            break
    p = i
    q = j
    while i<j:
        if a[i] == a[j]:
            i+=1
            j-=1
        elif a[i] == le:
            i+=1
        elif a[j] == le:
            j-=1
        else:
            c = 0
            break
    if c == 1:
        print("YES")
        continue
    c = 1
    while p<q:
        if a[p] == a[q]:
            p+=1
            q-=1
        elif a[q] == ri:
            q-=1
        elif a[p] == ri:
            p+=1
        else:
            c = 0
            break
    if c == 0:
        print("NO")
    else:
        print("YES")