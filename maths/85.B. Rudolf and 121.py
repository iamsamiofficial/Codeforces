
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    i = 1
    while i <n-1:
        if l[i-1] <0 or l[i] < 0 or l[i+1] <0:
            break
        if l[i-1]>0 and l[i]>1 and l[i+1]>0:
            
            l[i+1]-=l[i-1]
            l[i]-=2*l[i-1]
            l[i-1] = 0
        i+=1
    if not any(l):
        print('YES')
    else:
        print('NO')