r,c = map(int,input().split())

for i in range(1,r+1):
    list2 = []
    for j in range(c):
        if i%2 == 0:
            list2.append(".")
        else:
            list2.append("#")
    for j in range(c):
        if i%4 == 2:
            list2[-1] = '#'
        elif i%4 == 0:
            list2[0] = '#'
    print("".join(list2))

