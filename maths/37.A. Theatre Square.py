import math
x,y,z = map(int,input().split())

p = math.ceil(x/z)
n= math.ceil(y/z)
print(p*n)