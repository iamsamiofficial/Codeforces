import math
from decimal import Decimal,getcontext
getcontext().prec = 50
for _ in range(int(input())):
    x,y,k = map(int,input().split())
    
    lge = (Decimal(k)*Decimal(y))+Decimal(k)
    ans = math.ceil((lge-x)/Decimal((x-1)))
    
    
    
    print(ans+1+k)