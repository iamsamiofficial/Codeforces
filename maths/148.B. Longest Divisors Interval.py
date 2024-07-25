for _ in range(int(input())):
    n = int(input())
    i = 1
    ans = 0
    while n%i == 0:
        ans+=1
        i+=1
    print(ans)