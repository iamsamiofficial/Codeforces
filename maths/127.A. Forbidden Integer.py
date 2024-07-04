
for _ in range(int(input())):
    n,k,x = map(int,input().split())
    ans = []
    if x== 1 and k == 1:
        print("NO")
    elif x == 1 and k == 2 and n%k != 0:
        print("NO")
    elif x!=1:
        print("YES")
        print(n)
        print(*([1]*n))
    elif n%2 == 0:
        print("YES")
        print(n//2)
        print(*([2]*(n//2)))
    elif n%2 == 1:
        for i in range((n-3)//2):
            ans.append(2)
        ans.append(3)
        print("YES")
        print(len(ans))
        print(*ans)