n = int(input())

i = 1
s1 =[]
s2 = []

if n<3:
    print("No")
else:
    while i<=n:
        if i%2 == 0:
            s1.append(i)
        else:
            s2.append(i)
        i+=1
    print("Yes")
    print(len(s1),*s1)
    print(len(s2),*s2)