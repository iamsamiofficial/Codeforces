def threenumber():
    a,b,c,d = map(int,input().split())

    if a>b and a>c and a>d:
        print(a-b,a-c,a-d)
    elif b>a and b>c and b>d:
        print(b-a,b-c,b-d)
    elif c>a and c>b and c>d:
        print(c-a,c-b,c-d)
    else:
        print(d-a,d-b,d-c)

sam = threenumber()

    