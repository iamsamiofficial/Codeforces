for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        p = input()
        l.append([i for i in p])
    i = 0
    le = n
    c = 0
    while i <le:
        j = i
        bl = le-1
        while j<le-1:
            o = 0
            z = 0
            if l[i][j] =="0":
                z+=1
            else:
                o+=1
            if l[bl][i] =="0":
                z+=1
            else:
                o+=1
            if l[le-1][bl]=="0":
                z+=1
            else:
                o+=1
            if l[j][le-1] == "0":
                z+=1
            else:
                o+=1
            c+=(min(o,z))
            j+=1
            bl-=1
           
        le-=1
        i+=1

    print(c)

