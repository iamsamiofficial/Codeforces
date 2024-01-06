t = int(input())
for _ in range(t):
    n = int(input())
    f = int(str(n)[0])
    j = f-1
    j = j*10
    k = len(str(n))
    j = j+((k*(k+1)/2))
    print(int(j))
