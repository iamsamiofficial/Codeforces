x = input()
arr = [int(num) for num in x ]

for i in range(len(x)):
    if ((9-arr[i])> arr[i] or 9-arr[i] == 0) and i == 0:
        arr[i] = arr[i]
    elif (9-arr[i]>arr[i]):
        arr[i] = arr[i]
    else:
        arr[i] = (9-arr[i])
print("".join(map(str,arr)))