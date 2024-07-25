
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,n-1):
        if a[i-1]< a[i] and a[i]>a[i+1]:
            ans = 1
            print("YES")
            print(i,i+1,i+2)
            break
    if ans == 0:
        print("NO")
        