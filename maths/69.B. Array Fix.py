
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0

    if l == sorted(l):
        print("YES")
    else:
        i = 0
        while i <len(l):
            if l[i]<10:
                i+=1
            else:
                l = l[:i]+[l[i]//10]+[l[i]%10]+l[i+1:]
                i+=1
                
                if l==sorted(l):
                    c = 1
                    break
                
        if c == 1:
            print("YES")
        else:
            print("NO")
