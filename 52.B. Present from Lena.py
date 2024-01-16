# # n = int(input())
# # arr = []
# # for i in range(n):
# #     arr.append(i)
# # for i in range(n,-1,-1):
# #     arr.append(i)
# # p = len(arr)
# # for i in range(n):
# #     store = []
# #     store.append(arr[:i+1])
# #     if p < len(arr):
# #         store.append(arr[p:])
# #     p-=1
    
# #     #print(" ".join(map(str,store)))
# #     final = [str(element) for sub in store for element in sub]
# #     print(" ".join(map(str, final)))
# # print(" ".join(map(str,arr)))



# n = int(input())

# for i in range(n+1):

#     j = i
#     while j<n:
#         print("  ",end="")
#         j+=1
#     j = 0
#     while j<=i:
#         print(j,end="")
        
#         if i!=j:
#             print(" ",end="")
#         j+=1
#     j = i-1
#     while j>=0:
#         print(" ",end="")
#         print(j,end="")
#         j-=1
    
#     print()

# for i in range(n):
#     j = 0

#     while j<=i:
#         print("  ",end="")
#         j+=1
#     j = 0
#     while j < n-i:
#         print(j,end="")
#         if j != (n-i-1):
#             print(" ",end="")
#         j+=1
#     j = n-i-2
#     while j >= 0:
#         print(" ",end="")
#         print(j,end="")
#         j-=1
#     print()
    


n = int(input())
row = -n
while row<=n:

    i = 0
    while i<abs(row):
        print("  ",end="")
        i+=1

    maxi = n-abs(row)
    i = 0
    while i <maxi:
        print(i,end=" ")
        i+=1
    i = maxi
    while i>0:
        print(i,end=" ")
        i-=1

    print(0,end="")

    row+=1
    print()

    

    