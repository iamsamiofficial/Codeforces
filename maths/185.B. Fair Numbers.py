def d(n):
    y = n
    while y:
        
        a = y%10
        if a!=0 and n%a!=0:
            return False
        y = y//10
    return True

for _ in range(int(input())):
    n = int(input())

    while not(d(n)):
        n+=1
    print(n)