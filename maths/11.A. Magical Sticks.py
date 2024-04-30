t = int(input())
import math
for _ in range(t):
    n = int(input())

    if n<=2:
        print(1)
    else:
        print(math.ceil(n/2))