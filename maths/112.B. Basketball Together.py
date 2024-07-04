
# n,d = map(int,input().split())
# l = list(map(int,input().split()))
# l.sort()
# i = 1        
# j = n-1
# ans = 0
# p = l[j]       # 6 180
# #100 90 80 70 60 50 
# while i <=n:
#     if p>d:
#         ans+=1
#         j-=1
#         p = l[j]
#         i+=1
#     else:
#         p+=l[j]
#         i+=1
        
# print(ans)


# Read input
results = []
t = int(input())
for _ in range(t):
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
  
    
    initial_diff = x1 - y1
    final_diff = x2 - y2
    
    # Check if the difference maintains the same sign and is non-zero
    if (initial_diff * final_diff > 0) or (x1 == x2 and y1 == y2):
        results.append("YES")
    else:
        results.append("NO")

# Print results
for result in results:
    print(result)
