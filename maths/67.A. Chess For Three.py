
# for _ in range(int(input())):
#     p1,p2,p3 = map(int,input().split())

#     if (p1+p2+p3)%2 != 0:
#         print(-1)
#     else:
#         print((p1+p2+p3)//2)
results = []
for i in range(int(input())):
    
    p1, p2, p3 = map(int,input().split())
    S = p1 + p2 + p3
        
    if S % 2 != 0:
        results.append(-1)
        continue
        
    G = S // 2  # Total number of games
        
    
    if p3 > G:
        results.append(-1)
    else:
        results.append(p3)
    
for i in results:
    print(i)
