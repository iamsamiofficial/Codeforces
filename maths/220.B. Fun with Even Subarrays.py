for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))[::-1]
 
    c = 0
    i = 1
    while i <len(p):
        if p[i]!=p[i-1]:
            c+=1
            i*=2
            if i < n:
                p[i-1] = p[0]
        else:
            i+=1
    print(c)
    
