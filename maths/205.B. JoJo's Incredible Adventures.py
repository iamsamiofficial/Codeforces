for _ in range(int(input())):
    s = input()
    mx = 0
    c =0
    for j in range(2*len(s)-1):
        if s[j%len(s)] == "1":
            c+=1
            mx = max(mx,c)
        else:
            c = 0
    if mx == len(s):
        print(mx*mx)
        continue
    if mx&1:
        print(((mx+1)//2)*((mx+1)//2))
        continue
    print((mx//2)*((mx//2)+1))