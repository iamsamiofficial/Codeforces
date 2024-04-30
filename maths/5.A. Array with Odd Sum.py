t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))

    summ = sum(l)
    c = 0
    if summ%2 == 1:
        print("YES")
    else:
        for i in range(1,len(l)):
            if l[0]%2 == 0:
                if l[i]%2==1:
                    c = 1
                    break
                
            else:
                if l[i]%2 == 0:
                    c=1
                    break
                
        if c == 1:
            print("YES")
        else:
            print("NO")