t  = int(input())

for _ in range(t):
    s = input()
    h = input()
    p = "".join(sorted(s))
    c = 0
    for i in range((len(h)-len(s))+1):
        j = "".join(sorted(h[i:i+len(s)]))

        if p == j:
            c = 1
            break
    if c == 1:
        print("YES")
    else:
        print("NO")