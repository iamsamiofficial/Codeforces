for _ in range(int(input())):
    a,b,c = map(int,input().split())
   
    if (a+b+c)%9 == 0 and min(a,b,c)>= (a+b+c)/9:
        print('yes')
    else:
        print('no')