for _ in range(int(input())):
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x&1:
        if y%4 == 0:
            print(x)
        elif y%4 == 1:
            print(x+y)
        elif y%4 == 2:
            print(x-1)
        elif y%4 == 3:
            print(x-(y+1))
    else:
        if y%4 == 0:
            print(x)
        elif y%4 == 1:
            print(x-y)
        elif y%4 == 2:
            print(x+1)
        elif y%4 ==3:
            print(x+y+1)