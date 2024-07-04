b = [int(bin(i)[2:]) for i in range(2,64)]

for _ in range(int(input())):
    n = int(input())
    if n in b:
        print("YES")
    else:
        for i in b:
            while n>1 and n%i == 0:
                n/=i
        if n == 1:
            print("YES")
        else:
            print("NO")

    
    