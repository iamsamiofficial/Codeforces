for _ in range(int(input())):
    n = int(input())
    w = list(map(int,input().split()))
    
    c = 0
    pre = [0]
    
    for i in w:
        pre.append(pre[-1]+i)
    i = 1
    j = n-1
    while i<=j:
        if pre[i]>(pre[-1]-pre[j]):
            j-=1
        elif pre[i]<(pre[-1]-pre[j]):
            i+=1
        else:
            c = (i)+(n-(j))
            i+=1
            j-=1
            
    print(c)
