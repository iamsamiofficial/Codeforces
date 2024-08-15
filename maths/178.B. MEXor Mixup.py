for _ in range(int(input())):
    a,b = input().split()
    c = int(a)
    a = int(a)-1
    if a%4 == 0:
        a = a
    elif a%4 == 3:
        a = 0
    elif a%4 == 2:
        a = (a+2)-1
    else:
        a = 1

    b = int(b)
    if a == b:
        print(c)
    elif a ^c == b:
        print(c+2)
    else:
        print(c+1)