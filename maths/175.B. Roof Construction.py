import math

for _ in range(int(input())):
    n = int(input())-1
    #b = 2**(int(math.log2(n)))
    b = 1<<(n.bit_length()-1)
    a = []
    for i in range(1,b):
        a.append(i)
    a.append(0)
    for i in range(b,n+1):
        a.append(i)
    print(*a)