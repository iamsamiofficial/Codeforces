
from collections import Counter
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list( map(int,input().split()))
    l1 = sorted(l[:n])
    l2 = sorted(l[n:2*n])
    c1 =[]
    dup1 = []
    dup2 = []
    if l1 == l2:
        print(*l1[:2*k])
        print(*l1[:2*k])
    else:
        c1 = Counter(l1)
        c2 = Counter(l2)
        dup1 = [item for item in l1 if c1[item]>1]
        dup2 = [item for item in l2 if c2[item]>1]
        single = [item for item in l1 if c1[item]==1]
        # i = 0
        # while i <(len(l1)-1):
        #     if l1[i] == l1[i+1]:
        #         dup1.append(l1[i])
        #         dup1.append(l1[i])
        #         i+=2
        #     else: 
        #         c1.append(l1[i])
        #         if i == len(l1)-2:
        #             c1.append(l1[i+1])
        #         i+=1
        # i = 0
        # while i <(len(l2)-1):
        #     if l2[i] == l2[i+1]:
        #         dup2.append(l2[i])
        #         dup2.append(l2[i])
        #         i+=2
        #     else:
        #         i+=1
        
        if len(dup1) >= 2*k:
            print(*dup1[:2*k])
            print(*dup2[:2*k])
        else:
            print(*(dup1+single[:((2*k)-len(dup1))]))
            print(*(dup2+single[:((2*k)-len(dup2))]))

