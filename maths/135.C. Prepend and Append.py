for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    while i<n-i-1 and s[i]!=s[n-i-1]:
        i+=1
    print(n-2*i)
            
