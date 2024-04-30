# x,y = map(int,input().split())

# ans = 1
# i = 2
# z = x
# if x<10 and y%x == 0:
#     print(int(y/x))



# else:
#     while (z-y)%10!=0 and z%10 !=0:
#         z = x*i
#         ans+=1
#         i+=1
#     print(ans)

def sami():
    
    x,y = map(int,input().split())
    i = 1

    while i<10:
        p = x*i
        if p%10 == 0 or p%10 ==y:
            return i
        i+=1
    return i
sam = sami()
print(sam)
    