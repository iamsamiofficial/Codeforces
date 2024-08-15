prime = [0]*(10**7)

i = 2
while i<len(prime):
    if prime[i] == 0:
        j = i*2
        while j<len(prime):
            prime[j] = 1
            j+=i
    i+=1

for _ in range(int(input())):
    d = int(input())
    b = 1
    c = b+d
    e = c+d
    for i in range(c,len(prime)):
        if prime[i] == 0:
            c = i
            break
    for i in range(c+d,len(prime)):
        if prime[i] == 0:
            e = i
            break
    print(c*e)








