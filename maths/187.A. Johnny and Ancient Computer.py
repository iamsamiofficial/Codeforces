from decimal import Decimal,getcontext
getcontext().prec = 50
for _ in range(int(input())):
    x,y = input().split()
    x = int(Decimal(x))
    y = int(Decimal(y))
    x2 = min(x,y)
    y2 = max(x,y)
    p = 0
    while x2<y2:
        if (x2*2 == y2 or x2 *4 == y2 or x2*8 == y2):
            p+=1
            break
        x2 = x2*8
        p+=1
        if x2>y2:
            p = -1
            break
    print(p)
