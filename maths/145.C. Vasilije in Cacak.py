
for _ in range(int(input())):
    n,k,x = map(int,input().split())
    a = (k*(k+1))//2
    b = ((n*(n+1))//2) - (((n-k)*(n-k+1))//2)
    if x<a or x>b:
        print("NO")
        continue
    print("YES")