for _ in range(int(input())):
    n = int(input())
    if n&1 or n<4:
        print(-1)
        continue
    # maxi = n//4
    # mini = n//6
    # if n%6 == 2 and n-8>-1:
    #     mini = ((n-8)//6) + 2
    # elif n%6 == 4 and n-4>-1:
    #     mini = ((n-4)//6)+1
    # print(mini,maxi)
    if n == 4:
        print(1,1)
        continue
    if n == 6:
        print(1,1)
        continue
    if n == 8:
        print(2,2)
        continue
    if n == 10:
        print(1,1)
        continue
    
    if n%4 == 0:
        maxi = n//4
    if n%4 == 2:
        p = n-6
        maxi = (p//4)+1
    
    if n%6 == 0:
        mini = n//6
    if n%6 == 2:
        q = n - 8
        mini = (q//6)+2
    if n%6 == 4:
        r = n-4
        mini = (r//6)+1
    print(mini,maxi)