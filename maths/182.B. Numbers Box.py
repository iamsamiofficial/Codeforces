for _ in range(int(input())):
    n,m = input().split()
    n = int(n)
    m = int(m)
    ans = []
    c = 0
    for i in range(n):
        a = list(map(int,input().split()))
        for i in a:
            if i <0:
                c+=1
            ans.append(abs(i))
    if c&1:
        print(sum(ans)-2*min(ans))
        continue
    print(sum(ans))