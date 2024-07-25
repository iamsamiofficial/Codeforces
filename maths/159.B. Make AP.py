for _ in range(int(input())):
    a,b,c = map(int,input().split())
    
    m1 = (2*b-c)
    m2 = (c+a)
    m3 = (2*b-a)
    if m1%a == 0 and m1//a >0 :
        print("YES")
    elif m2%(2*b) == 0:
        print("YES")
    elif m3%c == 0 and m3//c>0:
        print("YES")
    else:
        print("NO")
         

