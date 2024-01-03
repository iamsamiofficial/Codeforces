t = int(input())

for _ in range(t):
    s = input()
    p = s[1:len(s)-1]
    if len(s) >10:
        n =s[0]+str(len(p))+s[-1]
        print(n)
    else:
        print(s)