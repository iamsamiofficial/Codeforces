
# m = int(input())
# n = list(map(int,input().split()))

# prev = 0
# energy = 0
# result = 0
# for i in range(len(n)):
#     energy += prev-n[i]
#     if energy < 0:
#         result -=energy
#         energy = 0
#     prev = n[i]
# print(result)
m = int(input())
n = list(map(int,input().split()))
 
 
energy = 0
height = n[0]#3 4 3 2 4
dollar = n[0]
i = 0
j = 1
 
for i in range(len(n)-1):
    if n[i]-n[j] <0 and energy<=0:
        dollar+=n[j]-n[i]
        energy = 0
    elif n[i]-n[j]<0 and energy>0:
        energy-=n[i]-n[j]
    else:
        energy+=n[i]-n[j]
    j+=1
print(dollar)