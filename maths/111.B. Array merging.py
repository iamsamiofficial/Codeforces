from itertools import groupby
import math
from collections import Counter

# t = int(input())  # Number of test cases
# for _ in range(t):
#     n, m = map(int, input().split())  # Length of string s and number of updates
#     s = input().strip()  # The string s
#     ind = list(map(int, input().split()))  # Indices to update
#     c = input().strip()  # Characters for updates
    
#     # Dictionary to store updates
#     updates = {}
#     for i in range(m):
#         idx = ind[i] - 1  # Convert to 0-based index
#         char = c[i]
#         if idx not in updates or char < updates[idx]:
#             updates[idx] = char
    
#     # Apply updates to string s
#     result = list(s)
#     for idx, char in updates.items():
#         result[idx] = char
    
#     # Output the result for this test case
#     print(''.join(result))


# results = []

# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     s = input()
#     s = list(s)
#     indices = list(map(int,input().split()))
    
    
#     characters = input()
    
#     # Sort indices and characters
#     sorted_indices = sorted(indices)
#     sorted_characters = sorted(characters)
    
#     # Apply sorted updates
#     for i in range(m):
#         s[sorted_indices[i] - 1] = sorted_characters[i]
    
#     results.append("".join(s))

# # Output results
# for i in results:
#     print(i)


# def find_local_maxima_cpp_style(array):
#     rows, cols = len(array), len(array[0])
#       # Initialize result array
    
#     for i in range(rows):
#         for j in range(cols):
#             val = 0  # Store current maximum value found
#             # Check neighbors within array bounds
#             f = 1
#             if i-1 >= 0:
#                 val = max(val, array[i-1][j])
#             if i+1 < rows:
#                 val = max(val, array[i+1][j])
#             if j-1 >= 0:
#                 val = max(val, array[i][j-1])
#             if j+1 < cols:
#                 val = max(val, array[i][j+1])

#             # Check if current element is a local maxima (replace with 0 for max)
#               # Flag to indicate local maxima
#             if i-1 >= 0 and array[i][j] <= array[i-1][j]:
#                 f = 0
#             if i +1< rows and array[i][j] <= array[i+1][j]:
#                 f = 0
#             if j -1>= 0 and array[i][j] <= array[i][j-1]:
#                 f = 0
#             if j+1 < cols and array[i][j] <= array[i][j+1]:
#                 f = 0

#             # Update result (replace with 0 for local maxima)
#             if f:
#                 array[i][j] = val

#     return array

# # Read number of test cases
# num_cases = int(input())

# for _ in range(num_cases):
#     n, m = map(int, input().split())
#     matrix = []
    
#     for i in range(n):  # read n rows
#         row = list(map(int, input().split()))
#         matrix.append(row)
    
#     local_maxima = find_local_maxima_cpp_style(matrix)
    
#     # Print the local maxima matrix
#     for row in local_maxima:
#         print(' '.join(map(str, row)))

from itertools import groupby
from collections import Counter,defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = defaultdict(int)
    ans = 0
    for i,j in groupby(a):
        d[i] = max(d[i],len(list(j)))
        ans = max(ans,d[i])
    
    for i,j in groupby(b):
        length = len(list(j))
       
        ans = max(ans,d[i]+length)
    print(ans)
    



