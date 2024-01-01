import numpy as np
def prime():
    store = []
    num_values = 87000009
    arr = np.full(num_values,True,dtype=bool)
    n = 87000008

    arr[0] = arr[1] = False
    i = 2
    while (i*i<=n):
        if (arr[i]):
            j = i*i
            while j<= n:
                arr[j] = False
                j+=i
        i+=1
    for i in range(2,num_values):
        if arr[i]:
            store.append(i)
    return store      
        
def main(pr, q):
    primes = pr()
    for _ in range(q):
        n = int(input())

        print(primes[n - 1])


q = int(input())
m = main(prime, q)
