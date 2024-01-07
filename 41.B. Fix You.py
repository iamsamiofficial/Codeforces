t = int(input())
for _ in range(t):
    r,c = map(int,input().split())
    p = 0
    list1 = []
    for i in range(r):
        s = input().upper()
        list2 = [i for i in s]
        list1.append(list2)
    for j in range(c):
        if list1[r-1][j] == "D":
            p+=1
    for i in range(r):
        if list1[i][-1] == "R":
            p+=1
    print(p)

