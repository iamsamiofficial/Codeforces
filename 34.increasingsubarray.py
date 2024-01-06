n = int(input())

l = list(map(int,input().split()))
maxi = 0
if len(l) == 1:
    print(1)
else:
    j = 1
    c = 0
    for i in range(n-1):
        if l[j] > l[i]:
            c+=1
            maxi = max(maxi,c)
        else:
            c = 0
        j+=1
    print(maxi+1)

