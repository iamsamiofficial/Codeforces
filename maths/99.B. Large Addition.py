for _ in range(int(input())):
    n = input()
    m = n[0]
    j = n[-1]
    p = n[:len(n)-1]
    if m=="1" and j!="9" and "0" not in p:
        print("YES")
    else:
        print("NO")
        