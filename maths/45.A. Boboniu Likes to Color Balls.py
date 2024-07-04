
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())

    if d%2 == 0 and a%2 == 0 and b%2 == 0 and c%2 ==0:
        print("Yes")
    elif d%2 == 0 and a%2 == 1 and b%2 ==1 and c%2 == 1:
        print("Yes")
    elif d%2 == 1 and a%2 == 0 and b%2 == 0 and c%2 ==0:
        print("Yes")
    
    elif d%2 == 1 and a%2 == 1 and b%2 ==1 and c%2 == 1:
        print("Yes")
    elif d%2 == 1 and a%2 == 1 and b%2 ==1 and c%2 == 0 and c !=0:
        print("Yes")
    elif d%2 == 1 and a%2 == 1 and b%2 ==0 and c%2 == 1 and b !=0:
        print("Yes")
    elif d%2 == 1 and a%2 == 0 and b%2 ==1 and c%2 == 1 and a !=0:
        print("Yes")
    else:
        print("No")
        


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     x = list(map(int, input().split()))

#     a = [0] * n
#     a[0] = 501
#     for i in range(1,n):
#         a[i] = a[i-1]+x[i-1]
#     print(*a)

    # for i in range(1, n):
    #     a[i] = x[i-1] + a[i-1]

    # print(*a)



