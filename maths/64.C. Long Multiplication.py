
for _ in range(int(input())):
    x = input()
    y = input()
    a = ""
    b = ""
    n = min(x,y)
    z = max(x,y)
    i = 0
    while i <len(n):
        if z[i]> n[i]:
            a+=z[i]
            b+=n[i]
            break
        else:
            a+=z[i]
            b+=n[i]

        i+=1
        
    j = i+1

    while j <len(n):
        if z[j]> n[j]:
            a+=n[j]
            b+=z[j]
        else:
            a+=z[j]
            b+=n[j]
        j+=1
    print(a)
    print(b)

    