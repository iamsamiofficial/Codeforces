for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    # for i in range(n):
    #     l[i] = 2**l[i]
    
    # for i in range(1,n):
    #     l[i] = l[i] +l[i-1]
    # c = 0
    # for i in range(1,n):
    #     for j in range(i,n):
    #         if l[i]-l[i-1] == l[j]-l[i] or l[i-1] == l[j]-l[i-1] :
    #             c = 1
    #             break
    #         if l[i]-l[i-1] < l[j]-l[i] or l[i-1] < l[j]-l[i-1] :
    #             break

    #     if c == 1:
    #         break
    if n!= len(set(l)):
        print("YES")
        continue
    print("NO")
    
    # if c == 1:
    #     print("YES")
    #     continue
    # print("NO")
