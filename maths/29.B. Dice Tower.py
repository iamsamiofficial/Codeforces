input()

for i in (map(int,input().split())):
    print('NYOE S'[i > 14 and 0<i%14<=6 ::2])