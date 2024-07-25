for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    if l[0]!=l[-1]:
        print("YES")
        print(l[-1],l[0],*l[1:n-1])
    else:
        print("NO")
    # c = 0
    # if l[1] == l[0]:
    #     for i in range(2,n):
    #         if l[i] != l[1]:
    #             l[i],l[1] = l[1],l[i]
    #             c = 1
    #             break
    #     if c  == 1:
    #         print("YES")
    #         print(*l)
    #     else:
    #         print("NO")
    # else:
    #     print("YES")
    #     print(*l)