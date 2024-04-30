t = int(input())

for _ in range(t):
    m,n = map(int,input().split())

    mul = m*n

    
    
    if mul%2 ==0:
        print(int(mul/2))
    else:
        print(int(mul/2)+1)