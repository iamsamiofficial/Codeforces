n, k, l, c, d, p, nl, np = map(int,input().split())
arr = []
m = k*l

arr.append(m//nl)
arr.append(c*d)
arr.append(p//np)
final = min(arr)//n
print(final)
