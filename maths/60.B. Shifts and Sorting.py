
for _ in range(int(input())):
    n = input()
    i = 0
    ans = 0
    while i <len(n):
        if n[i] == "1":
            p = i
            break
        i+=1
    j = i+1
    while j< len(n):
        if n[j] == "0":
            ans += (j-i)+1
            i+=1
        j+=1
    print(ans)