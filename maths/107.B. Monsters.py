
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    for i in range(len(l)):
        if l[i]%k !=0:   
            l[i] = l[i]%k
        else:
            l[i] = k
    
    f = list(enumerate(l))
    f = sorted(f,key=lambda x:x[1],reverse=True)
    f = [i+1 for i,j in f]
    

    print(*f)