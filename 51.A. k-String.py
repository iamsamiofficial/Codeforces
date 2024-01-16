k = int(input())
dic = {}
s = input()
res = ""
if len(s)%k == 0:
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    for i in range(k):
        for key,value in dic.items():
            if value%k != 0:
                print(-1)
                exit()
            else:
                t = value//k
                for i in range(t):
                    res+=key
    print(res)

else:
    print(-1)