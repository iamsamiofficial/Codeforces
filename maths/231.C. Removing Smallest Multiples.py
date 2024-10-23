for _ in range(int(input())):
    n = int(input())
    s = input()
    t = []
    p = []
    ans = 0
    for i in range(len(s)):
        p.append(s[i])
        if s[i] == "0":
            t.append(i+1)
    for i in t:
        j = i
        while (j-1) <len(s):
            if s[j-1] == "0"and p[j-1] == "0":
                p[j-1] = "1"
                ans+=i
                j+=i
            elif s[j-1] == "0" and p[j-1] == "1":
                j+=i
            else:
                break
    print(ans)

