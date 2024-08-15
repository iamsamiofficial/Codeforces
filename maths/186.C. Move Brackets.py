for _ in range(int(input())):
    n = int(input())
    s = input()
    # sp = []
    # for i in range(n):
    #     if not sp:
    #         sp.append(s[i])
    #         continue
    #     if sp[-1] == "(" and s[i] == ")":
    #         sp.pop()
    #     else:
    #         sp.append(s[i])
    # print(len(sp)//2)

    while "()" in s:
        s = s.replace("()","")
    print(len(s)//2)
        
