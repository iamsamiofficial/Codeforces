t = int(input())

for _ in range(t):
    n = int(input())
    a = n
    b = n-1
    print(2)
    while b>=1:
        print(a,b)
        a = int((a+b+1)/2)
        b-=1

