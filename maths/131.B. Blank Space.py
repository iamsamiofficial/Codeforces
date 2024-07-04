# from itertools import groupby
# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     c = 0
#     g = [(key,list(value)) for key,value in groupby(l)]

#     for key,value in g:
#         if key == 0:
#             c = max(c,len(value))
#     print(c)

for _ in range(int(input())):
    # n = int(input())
    # s = input().split()
    # g = 0
    # c = 0
    # for i in s:
    #     if i == "0":
    #         c+=1
    #         g = max(g,c)
    #     else:
    #         c = 0
    # print(g)
    input()
    print(max(list(map(len,input().replace(" ","").split("1")))))