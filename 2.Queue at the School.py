x,y = input().split()
x = int(x)
y = int(y)

st = input()
sy = list(st)
#print(sy)

for i in range(y):
    j = 0
    while j<len(sy)-1:
        if sy[j] == "B" and sy[j+1] == "G":
            sy[j],sy[j+1] = sy[j+1],sy[j]
            j+=2
        else:
            j+=1
final = "".join(sy)
print(final)


