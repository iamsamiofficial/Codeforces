
for _ in range(int(input())):
    n = input()
    c = 1
    t = 0
    for i in range(len(n)-1):
        if n[i]!=n[i+1]:
            c+=1
        if n[i] == "0" and n[i+1] == "1":
            t = 1

    print(c-t)
