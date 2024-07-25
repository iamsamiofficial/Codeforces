for _ in range(int(input())):
    a,b = input().split()
    a = int(a)
    b = int(b)

    maxi = abs(a-b)
    if maxi == 0:
        print(0,0)
        continue
    mini = min(a%maxi, maxi - a%maxi)
    print(maxi,mini)