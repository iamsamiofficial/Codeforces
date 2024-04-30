import math

l = int(input())
if l>5 and l%2==0:
    n = l//2
    j = math.ceil(n/2)
    print(j-1)
else:
    print(0)