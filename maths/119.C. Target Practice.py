for _ in range(int(input())):
    ans = 0
    for i in range(10):
        a = input()
        for j in range(10):
            if a[j] == "X":
                ans+= min(i+1,10-i,j+1,10-j)
        
    print(ans)