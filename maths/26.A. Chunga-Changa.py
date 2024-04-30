x,y,z = map(int,input().split())
 
ans = (x+y)//z
an = (x//z)+(y//z)
if x%z == 0 or y%z == 0:
    mini = 0
else:
    if ans == an:
        mini = 0
    else:
        mini = min((z-(x%z)),(z-(y%z)))
print(ans,mini)