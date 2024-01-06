s = input()
i,j,k,l,m = map(str,input().split())
if s[0] == i[0] or s[0] == j[0] or s[0] == k[0] or s[0] == l[0] or s[0] == m[0] or s[1] == i[1] or s[1] == j[1] or s[1] == k[1] or s[1] == l[1] or s[1] == m[1]:
    print('YES')
else:
    print('NO')