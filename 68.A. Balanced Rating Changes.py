# n = int(input())
# arr1 = []
# arr = []
# for i in range(n):
#     p = int(input())
#     arr1.append(p//2)
#     arr.append(p)

# v = sum(arr1)

# if v == 0:
#     for i in arr1:
#         print(i)
# else:
#     i = 0
#     while v!=0:
#         if (arr[i])%2!=0:
#             arr1[i] = arr1[i]+1
#             if v<0:
#                 v+=1
#             else:
#                 v-=1
#         i+=1
#     for i in arr1:
#         print(i)

    

n = int(input())
odd = 0
arr = []
for i in range(n):
    p = int(input())
    arr.append(p)
    if p%2:
        odd+=1


odd = int(odd/2)

for i in range(len(arr)):
    if arr[i]%2:
        if odd>0:
            odd-=1
            arr[i] = arr[i]-1
        else:
            arr[i] = arr[i]+1


for i in arr:
    print(int(i/2))