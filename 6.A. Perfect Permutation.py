n = int(input())
arr = []
for i in range(n):
    arr.append(i+1)
#print(arr)

if len(arr)%2 == 0:
    arr = arr[::-1]
    for i in arr:
        print(i)
    
else:
   print(-1)