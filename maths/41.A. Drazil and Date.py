a,b,s = map(int,input().split())

if abs(a)+abs(b)<=s and (abs(s)-(abs(a)+abs(b)))%2 == 0:
    print("YES")
else:
    print("NO")
# else:
#     if a+b == s:
#         print("YES")
#     elif (s-(a+b))%2 == 0:
#         print("YES")
#     else:
#         print("NO")