n = int(input())
x = list(map(int,input().split()))
maxi = -1
mini = 9999999999
indmax = 0
indmin = 0
for i in range(n-1):
    if x[i] >= x[i+1]:
        if maxi >= x[i]:
            maxi = maxi
            indmax = indmax
        else:
            maxi = x[i]
            indmax = i
        
        if mini < x[i+1]:
            mini = mini
            indmin = indmin
        else:
            mini = x[i+1]
            indmin = i+1
    else:
        if maxi >= x[i+1]:
            maxi = maxi
            indmax = indmax
        else:
            maxi = x[i+1]
            indmax = i+1
        
        if mini < x[i]:
            mini = mini
            indmin = indmin
        else:
            mini = x[i]
            indmin = i

if indmax < indmin:
    final = indmax + (n-1-indmin)
else:
    final = indmax + (n-1-(indmin+1))
print(final)
