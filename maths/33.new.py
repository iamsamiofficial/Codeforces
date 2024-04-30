# t = int(input())  # Number of test cases

# for _ in range(t):
#     n = int(input())  # Length of the lost string
#     trace = list(map(int, input().split()))  # Trace of the string

#     s = ""  # Initialize empty string
#     counts = [0] * 26  # Initialize counts for each character

#     for i in range(n):
#         if trace[i] == 0:
            
#             for j in range(26):
#                 if counts[j] == 0:
#                     s += chr(ord('a') + j)
#                     counts[j] += 1
#                     break
#         else:
            
#             for j in range(26):
#                 if counts[j] == trace[i]:
#                     s += chr(ord('a') + j)
#                     counts[j] += 1
#                     break

#     print(s)



# for _ in range(int(input())):
#     n,m,k = map(int,input().split())
#     l1 = list(set((map(int,input().split()))))
#     l2 = list(set((map(int,input().split()))))
#     c1 = c2 = flag = 0

#     for i in range(1,k+1):
#         if i in l1 and i in l2:
#             c1+=1
#             c2+=1
#         elif i in l1:
#             c1+=1
#         elif i in l2:
#             c2+=1
#         else:
#             flag = 1
#             break
#     if flag == 1:
#         print("NO")
#     elif c1>=k//2 and c2>=k//2:
#         print("YES")
#     else:
#         print("NO")



# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     s = ""
#     c = 0
#     cl = [0]*n
#     for i in range(len(l)):
#         if l[i] == 0:
#             for j in range(26):
#                 if j>=c:
#                     s+= chr(ord("a")+j)
#                     c+=1
#                     cl[j]+=1
#                     break
#                                          #0 0 0 1 0 2 0 3 1 1 4
#         else:
#             for j in range(26):
#                 if l[i] == cl[j]:
#                     s+=chr(ord("a")+j)
#                     cl[j]+=1
#                     break
#     print(s)


for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    dic = {}
    res = ""
    for i in l:
        if i not in dic:
            dic[i] = 0
        res+= chr(ord('a')+dic[i])
        dic[i]+=1
    print(res)


