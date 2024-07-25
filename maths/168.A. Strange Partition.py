import math
for _ in range(int(input())):
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    store = 0
    maxi = 0
    for i in l:
        store+=i
        maxi+=math.ceil(i/x)
    print(math.ceil(store/x),maxi)