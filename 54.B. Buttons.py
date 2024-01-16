n = int(input())
c = n
for i in range(1,n):
    c+= i*(n-i)
print(c)