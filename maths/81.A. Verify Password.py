# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     digit = []
#     letter = []
#     for i in s:
#         if i.isdigit():
#             digit.append(i)

#         else:
#             letter.append(i)

#     if digit != sorted(digit):
#         print("NO")
#     elif letter != sorted(letter):
#         print("NO")
#     else:
#         combined = digit+letter
#         if "".join(combined) == s:
#             print("YES")
#         else:
#             print("NO")

import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    d = 0
    k = b[-1]
    sd = math.inf
    for i in range(len(a)):
        if (a[i] > k and b[i]< k) or (a[i]<k and b[i]>k):
            d = 1

        c+= abs(a[i]-b[i])
    if d == 1:
        c+=1
    else:
        p = a+b[:len(b)-1]
        if k in p:
            c+=1
        else:
            for i in range(len(a)):
                sd = min(sd,abs(k-a[i]),abs(k-b[i]))
            c+=1
            c+=sd
        

    print(c)

