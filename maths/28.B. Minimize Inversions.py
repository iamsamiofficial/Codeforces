for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    ans = list(zip(a,b))
    
    ans.sort()

    a = [i[0] for i in ans]
    b = [i[1] for i in ans]
    print(*a)
    print(*b)