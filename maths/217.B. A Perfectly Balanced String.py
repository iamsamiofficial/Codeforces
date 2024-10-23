for _ in range(int(input())):
    s = input()
    d = {}
    l = len(set(s))
    c = 0
    for i in range(len(s)):
        if s[i] in d.keys() and l>len(set(s[d[s[i]]:i+1])):
            c = 1
            break
        d[s[i]] = i
    if c == 0:
        print("YES")
        continue
    print("NO")            