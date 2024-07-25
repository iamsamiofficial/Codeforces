from collections import Counter
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    p = [count for item,count in Counter(s).items() if count%2 == 1]

    if k+1<len(p):
        print("NO")
        continue
    print("YES")