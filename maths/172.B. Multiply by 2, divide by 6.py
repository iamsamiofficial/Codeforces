for _ in range(int(input())):
    n = int(input())
    c = 0
    while n!=1:
        if n%6 == 0:
            c+=1
            n/=6
        elif n%6 == 3:
            c+=1
            n*=2
        else:
            break
    if n == 1:
        print(c)
        continue
    print(-1)