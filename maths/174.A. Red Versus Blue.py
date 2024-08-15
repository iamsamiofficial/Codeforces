import math
for _ in range(int(input())):
    n,r,b = map(int,input().split())
    s = ""
    j = math.floor(r/(b+1))
    k = r%(b+1)
    for i in range(k):
        s+=("R"*(j+1))
       
        s+="B"
    for i in range(k,b):
        s+=("R"*j)
        s+="B"
        
    
    s+= "R"*j
    print(s)
                