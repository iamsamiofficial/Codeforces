

for _ in range(int(input())):
    n,m = map(int,input().split())
    s = input()
    c = 0
    for i in "ABCDEFG":
        c+=max(0,(m-s.count(i)))
    print(c)

        
        