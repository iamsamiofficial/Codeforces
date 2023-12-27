x,y = input().split()
x = int(x)
y = int(y)

j = x+1
i = 2
c = 0
while i <j:
    if j%i != 0:
        i+=1
    else:
        j+=1
        i = 2
if j == y:
    print("YES")
else:
    print("NO")
# def isprime(j):
#     num = 2
#     while (num<j):
#         if j%num == 0:
#             return False
#         else:
#             num+=1
#     return True
# def para(x,y):
#     j = x+1
#     while j<=y:
#         if isprime(j):
#             break
#         else:
#             j+=1
#     if j == y:
#         return 'YES'
#     else:
#         return 'NO'
# x,y = input().split()
# final = para(int(x),int(y))
# print(final)
