

n = int(input())
ans = 0
while n>0:
    ans+= pow(2,n)
    n-=1
print(ans)