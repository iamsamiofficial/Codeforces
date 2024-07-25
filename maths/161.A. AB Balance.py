for _ in range(int(input())):
    s = input()
    print(s[:-1]+s[0])
    # a = 0
    # b = 0
    # for i in range(len(s)-1):
    #     if s[i] == "a" and s[i+1] == "b":
    #         a+=1
    #     elif s[i] == "b" and s[i+1] == "a":
    #         b+=1
    # if a == b:
    #     print(s)
    # else:
    #     if s[-1] == "a":
    #         print(s[:-1]+"b")
    #     else:
    #         print(s[:-1]+"a")