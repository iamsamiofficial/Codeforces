n = int(input())

i = 0

final = 0
p = 0

while final<n:
    i+=1
    final += i+p
    p+=i
if final > n:
    print(i-1)
else:
    print(i)