t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    i = 0
    j = n-1
    c = 1

    while i<j:

        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            if ord(s[i])<ord(s[j]):
                if chr(ord(s[i])+1) != chr(ord(s[j])-1):
                    c = 0
                    break
                    
            else:
                if chr(ord(s[i])-1) != chr(ord(s[j])+1):
                    c = 0
                    break
            i+=1
            j-=1
    if c == 1:
        print("YES")
    else:
        print("NO")

        