n = input()
a = n[0]
a = a.upper()
s = a
for i in range(1,len(n)):
    s+=n[i]
print(s)