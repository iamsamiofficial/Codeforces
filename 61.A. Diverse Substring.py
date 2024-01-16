n = int(input())
s = input()

c = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        c = 1
        break

if c == 1:
    print("YES")
    print(s[i]+s[i+1])
else:
    print("NO")

