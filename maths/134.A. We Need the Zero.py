
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
   
    j = l[0]
    for i in range(1,n):
        j^=l[i]
    
    if n&1:
        print(j)
        continue
    if j == 0:
        print(0)
        continue
    print(-1)
        