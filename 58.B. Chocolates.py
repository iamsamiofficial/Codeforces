n = int(input())
arr = list(map(int,input().split()))
ar = []
j = n-1
i = j-1
while i>=0:
    if arr[j]>arr[i]:
        i-=1
        j-=1
    else:
        if arr[j]-1 <= 0:
            arr[i] = 0
        else:
            arr[i] = arr[j]-1
        i-=1
        j-=1
# j = 0
# while j < n:
#     i = j+1
#     while i <n:
#         if arr[j]<arr[i]:
#             i+=1
#         else:
#             arr[j] = arr[i]-1#1 2 1 3 6
#             i= j+1
#     j+=1
print(sum(arr))
