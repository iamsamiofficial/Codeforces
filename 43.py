t = int(input())

for _ in range(t):
    c = 0
    n = int(input())
    s = input()
    for i in s:
        if i == "+":
            c+=1
        else:
            c-=1
    
    print(abs(c))