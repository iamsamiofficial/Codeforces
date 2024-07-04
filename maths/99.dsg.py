# # for _ in range(int(input())):
# #     x = input().split()
# #     y = x[1][0]+x[0][1]+x[0][2:]
# #     z = x[0][0]+x[1][1]+x[1][2:]
# #     print(y,z)

# # def find_max_multiple_sum(t, test_cases):
# #     results = []
    
# #     for n in test_cases:
# #         max_sum = 0
# #         best_x = 2
        
# #         for x in range(2, n + 1):
# #             k = n // x
# #             current_sum = x * (k * (k + 1)) // 2
            
# #             if current_sum > max_sum:
# #                 max_sum = current_sum
# #                 best_x = x
        
# #         results.append(best_x)
    
# #     return results

# # # Read input
# # t = int(input())
# # test_cases = [int(input()) for _ in range(t)]

# # # Get results
# # results = find_max_multiple_sum(t, test_cases)

# # # Print results
# # for result in results:
# #     print(result)


# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int,input().split()))
#     c = 0
#     for i in range(1,n+1):
#         s = 0
#         a = l[:i]
#         for j in range(len(a)):
#             if a[j] == sum(a)-a[j]:
#                 c+=1
#                 break
#     print(c)




# # Function to calculate Manhattan distance between two points
# def manhattan_distance(x1, y1, x2, y2):
#     return abs(x1 - x2) + abs(y1 - y2)

# # Function to find the center of the Manhattan circle
# def find_center(n, m, grid):
#     row_counts = [0] * n
#     col_counts = [0] * m

#     # Count the number of '#' in each row and column
#     for i in range(n):
#         for j in range(m):
#             if grid[i][j] == '#':
#                 row_counts[i] += 1
#                 col_counts[j] += 1

#     # Find the row and column with the maximum count
#     max_row_count = max(row_counts)
#     max_col_count = max(col_counts)
#     center_row = row_counts.index(max_row_count) + 1
#     center_col = col_counts.index(max_col_count) + 1

#     return center_row, center_col

# # Input the number of test cases
# t = int(input())

# # Iterate over each test case
# for _ in range(t):
#     # Input grid dimensions and the grid itself
#     n, m = map(int, input().split())
#     grid = [input() for _ in range(n)]

#     # Find and print the center of the Manhattan circle
#     center_row, center_col = find_center(n, m, grid)
#     print(center_row, center_col)



import math

# Function to calculate the number of distinct locations for a given dimension of S
def count_locations(x, y, z, k):
    locations = 0
    for i in range(1, min(x + 1, k // 3 + 1)):  # Iterate over possible x-coordinates of S
        for j in range(1, min(y + 1, k // (2 * i) + 1)):  # Iterate over possible y-coordinates of S
            z_range = min(z + 1, k // (i * j) + 1)  # Calculate possible z-coordinates of S
            locations += z_range  # Increment the count of locations
    return locations

# Input the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Input the dimensions of box B and volume k
    x, y, z, k = map(int, input().split())

    # Count the number of distinct locations for each valid dimension of S
    total_locations = 0
    for d in range(1, int(math.sqrt(k)) + 1):  # Iterate over possible dimensions of S
        if k % d == 0:  # Check if d divides k evenly
            total_locations += count_locations(x, y, z, d)  # Count locations for dimension d
            if d * d != k:  # Avoid counting the same dimension twice
                total_locations += count_locations(x, y, z, k // d)  # Count locations for dimension k // d

    # Output the total number of distinct locations for the current test case
    print(total_locations)

