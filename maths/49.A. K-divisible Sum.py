
import math
for _ in range(int(input())):
    x,y = map(int,input().split())
    
    z = math.ceil(x/y)
    y = y*z
    ans = math.ceil(y/x)
    print(ans)

    