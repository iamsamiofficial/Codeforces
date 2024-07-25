for _ in range(int(input())):
    s = input()
    z = 0
    f = 0
    ans = 0
    ans1 = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == "0":
            ans = i
            break
        else:
            z+=1
    for i in range(len(s)-1,-1,-1):
        if s[i] == "5":
            ans1 = i
            break
        else:
            f+=1

    for i in range(ans-1,-1,-1):
        if s[i] == "0" or s[i] == "5":
            break
        else:
            z+=1
    for i in range(ans1-1,-1,-1):
        if s[i] == "2" or s[i] == "7":
            break
        else:
            f+=1
    print(min(z,f))
        