t = int(input())

for _ in range(t):
    l = input()
    c = 0
    j = len(l)-1
    i = 0
    while i <len(l):
        if l[i] == "1":
            break
        i+=1
    while j >=0:
        if l[j] == '1':
            break
        j-=1  
    while i<=j:
        if l[i] == "0":
            c+=1
            i+=1
        elif l[j] == "0":
            c+=1
            j-=1
        else:
            i+=1
    print(c)