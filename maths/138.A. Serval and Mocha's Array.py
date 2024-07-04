import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    for i in l:
        for j in l:
            if math.gcd(i,j)<=2:
                c = 1
    if c == 1:
        print("YES")
    else:
        print("NO")
# import math
# print(math.gcd(6,6))