t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l = sorted(l)
    l1 = []
    l2 = []
    if n%2 != 0:
        i  = 0
        j = 1
        while j <len(l):
            l1.append(l[i])
            i+=2
            l2.append(l[j])
            j+=2
       
        sam = l1[int(n/2)]
        jam = l2[int(n/2)]

    else:
        p = n+1
        q = n -1
        i  = 0
        j = 1
        while j <len(l)-1:
            l1.append(l[i])
            i+=2
            l2.append(l[j])
            j+=2
        l1.append(l[-2])
        l1.append(l[-1])

        sam = l1[int(p/2)]
        jam = l2[int(q/2)]
    print(abs(sam-jam))
    
