for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if b>d:
        print(-1)
        continue
    if (b< 0 and d < 0) or (b>=0 and d>=0):
        s = abs(abs(d)-abs(b))
    else:
        s = abs(b)+abs(d)
    
    j = a+s
    if j<c:
        print(-1)
    elif  (j< 0 and c < 0) or (j>=0 and c>=0):
        print(s+abs(abs(j)-abs(c)))
    else:
        print(s+(abs(j)+abs(c)))