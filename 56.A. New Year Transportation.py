x,y = map(int,input().split())
l = list(map(int,input().split()))
c = 0
summ = 0
i = 0
while summ <=(y-1):
    if summ == (y-1):
        c=1
        break
    else:
        summ+=l[summ]
if c == 1:
    print('YES')
else:
    print('NO')


