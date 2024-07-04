
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(max(0,min((a[i+1]-a[i])//2+1 for i in range(n-1))))