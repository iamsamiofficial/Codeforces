s = input()
j = 0 
arr = []
while (j<len(s)-1):
    if s[j] == "-" and s[j+1] == ".":
        arr.append("1")
        j+=2
    elif s[j] == "-" and s[j+1] == "-":
        arr.append("2")
        j+=2
    else:
        arr.append("0")
        j+=1
if j == len(s)-1 and s[j] == ".":
    arr.append("0")
final = "".join(arr)

print(final)