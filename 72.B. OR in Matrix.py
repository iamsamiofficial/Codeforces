m,n = map(int,input().split())

matrix = []
matrix1 = []
sam = 0
for i in range(m):
    
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(m):
    row1 = []
    for j in range(n):
        if matrix[i][j] == 1:
            p = i
            q = 0
            while q<n:
                if matrix[i][q] == 0:
                    found = True
                    row1.append(0)
                    break
                else:
                    q+=1
                    found = False
                
                
            if found:
                continue
            else:
                q = 0
                
                while q<m:
                    if matrix[q][j] == 0:
                        found = True
                        row1.append(0)
                        break
                    else:
                        q+=1
                        found = False
            if found:
                continue
            else:
                row1.append(1)



        else:
            row1.append(0)
    matrix1.append(row1)

for i in range(m):
    for j in range(n):
        if matrix[i][j] == matrix1[i][j]:
            found = False

        else:
            p = i
            q = 0
            while q<n:
                if matrix1[i][q] == 1:
                    found = True
                    break
                else:
                    q+=1
                    found = False
                
                
            if found:
                continue
            else:
                q = 0
                
                while q<m:
                    if matrix1[q][j] == 1:
                        found = True
                        break
                    else:
                        q+=1
                        found = False
                if found:
                    continue
                else:
                    sam = 1
                    break
           
        if sam == 1:
            break
    if sam == 1:
        break

if sam == 1:
    print("NO")
else:
    print("YES")
    for i in range(m):
        print(*matrix1[i],sep=" ")
     


