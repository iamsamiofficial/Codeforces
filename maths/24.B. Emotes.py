n,m,k = map(int,input().split())

l = list(map(int,input().split()))
l.sort()

p = int(m/(k+1))
ans = (p*l[-2])
f = m-p
an = (f*l[-1])
print(an+ans)
    
