for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    f = 0
    b = 0
    d = 0

    if k == 1 or l[0] > l[k-1]:
        l[k-1],l[0] = l[0],l[k-1]
        for i in range(1,n):
            if l[0] > l[i]:
                f+=1
            else:
                break
    else:
        l[0],l[k-1] = l[k-1],l[0]
        for i in range(1,n):
            if l[0] >l[i]:
                f+=1
            else:
                break

        l[0],l[k-1] = l[k-1],l[0]
        for i in range(1,k):
            if l[i] > l[k-1]:
                l[k-1],l[i] = l[i],l[k-1]
                d = i
                b = 1
                break
        
        if d !=0:
            for i in range(d+1,k):
                if l[d] > l[i]:
                    b+=1
                else:
                    break
    print(max(f,b))




    

        

