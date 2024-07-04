
    
# for _ in range(int(input())):
#     x = int(input())
#     a = []
   
#     while x!=0:
#         if (x%2 !=0):
#             if (x%4) ==1:
#                 a.append(1)
#                 x-=1
#             else:
#                 a.append(-1)
#                 x+=1
#         else:
#             a.append(0)
        
#         x/=2
        
#     print(len(a))
#     print(*a)

for _ in range(int(input())):
    x = int(input())
    x = bin(x)[2:]
    x = reversed(x)
    x = list(x)
    ans = []
    d = 0
    i = 0
    t = 0
    while i <(len(x)-1):
        if x[i] =="1" and x[i+1] == "1":
            x[i] = "-1"
            j = i+1
            d = 1
            while j<len(x):
                if x[j] == "0":
                    x[j] = "1"
                    t = 1
                    d = 0
                    break
                else:
                    x[j] = "0"
                j+=1
        if t == 1:
            i = j
            t = 0
        else:
            i+=1
    if d ==1:
        x.append("1")
    print(len(x))
    print(*x)


    

# import math
# for _ in range(int(input())):
#     x = int(input())
#     if x&(x-1) == 0:
#         l = [0]*len(bin(x)[2:])
#         l[-1] = 1
#         print(len(l))
#         print(*l)
#         continue
#     j = 1<<x.bit_length()
#     l = ["0"]*len(bin(j)[2:])
#     l[-1] = "1"
#     p = j-x
#     p = bin(p)[2:]
#     p = p[::-1]
#     for i in range(len(p)):
#         if p[i] == "1":
#             l[i] = "-1"
#     print(len(l))
#     print(*l)
