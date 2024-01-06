t = int(input())

for _ in range(t):
    a,b,n = map(int,input().split())
    c = 0
    while a<= n and b<=n:
        if b>a:
            a+=b
            
        else:
            b+=a
        c+=1
    print(c)
           
    