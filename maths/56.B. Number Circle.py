
n = int(input())
l = list(map(int,input().split()))
c = 0
l.sort()

if l[0]+l[-2] > l[-1]:
    print("YES")
    print(*l)
else:
    if l[-2]+l[-3]>l[-1]:
        print("YES")
        l[-3],l[-1] = l[-1],l[-3]
        l[-2],l[-3] = l[-3],l[-2]
        print(*l)
    else:
        print("NO")
        
    

  