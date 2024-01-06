n = int(input())
s = input()
i = 0
p = ""
save = 0
while i <n:
    save = int(i*((i+1)/2))
    if save >= n:
        break
    else:
        
        p+=s[save]
    i+=1
print(p)


    
    