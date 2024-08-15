for _ in range(int(input())):
    a = input()
    b = input()
    p = 0
    if len(a)>len(b):
        m = a
        a = b
        b = m
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i:j+1] in b:
                p = max(p,j-i+1)
            else:
                break
        
    print((len(b)+len(a))-(2*p))
        




        