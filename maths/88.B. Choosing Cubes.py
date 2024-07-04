# def choosing_cubes(t, test_cases):
#     results = []
#     for i in range(t):
#         n, f, k, a = test_cases[i]
#         favorite_value = a[f - 1]
#         sorted_a = sorted(a, reverse=True)
        
#         greater_count = sum(1 for x in sorted_a if x > favorite_value)
#         equal_count = sum(1 for x in sorted_a if x == favorite_value)
        
#         if greater_count >= k:
#             results.append("NO")
#         elif greater_count + equal_count <= k:
#             results.append("YES")
#         else:
#             results.append("MAYBE")
    
#     return results

# # Reading input
# t = int(input().strip())
# test_cases = []
# for _ in range(t):
#     n, f, k = map(int, input().strip().split())
#     a = list(map(int, input().strip().split()))
#     test_cases.append((n, f, k, a))

# # Calculating results
# results = choosing_cubes(t, test_cases)

# # Printing results
# for result in results:
#     print(result)


for _ in range(int(input())):
    n,f,k = map(int,input().split())
    a = list(map(int,input().split()))

    p = a[f-1]
    a.sort()
    a = a[::-1]
    a1 = a[:k]
    a2 = a[k:]
    if p in a1 and p in a2:
        print('MAYBE')
    elif p in a1:
        print("YES")
    elif p in a2:
        print("NO")
