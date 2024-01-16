n = int(input())
s = ""
while n > 0 and n%7!=0:
    n-=4
    s+="4"
while n>0 and  n%7 == 0:
    n-=7
    s+="7"
if n == 0:
    print(s)
else:
    print(-1)
