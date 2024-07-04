

for _ in range(int(input())):
    n,k = map(int,input().split())

    if n&1 and k%2 ==0:
        print("NO")
        continue
    print("YES")