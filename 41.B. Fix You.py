t = int(input())
for _ in range(t):
    r,c = map(int,input().split())
    p = 0
    list1 = []
    for i in range(r):
        s = input().upper()
        list2 = [i for i in s]
        list1.append(list2)
    for j in range(c-1):
        if list1[0][j] == "D":
            p+=1
    if list1[0][-1] == "R":
        p+=1
    for i in range(1,r):
        if list1[i][-1] == "R":
            p+=1
    print(p)

