



# for _ in range(int(input())):
#     l,r = map(int,input().split())
    
#     x = r
#     score = 0
    
#     while x > 1:
#         score+=1
#         x //= 2
#     print(score)
import math
for _ in range(int(input())):
    l,r = map(int,input().split())
    ans = math.log2(r)
    print(int(ans))
        
