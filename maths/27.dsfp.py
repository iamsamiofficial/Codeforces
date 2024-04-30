# n = int(input())

# for i in range(n):
#     x,y = map(int,input().split())
#     if y <=1:
#         print(-2)
#     else:
#         if y%2 == 0:
#             z = int(y/2)
#             print(x*z)
#         else:
#             y = y-1
#             z = int(y/2)
#             print(x*z)

def minimize_inversions(t, test_cases):
    results = []

    for _ in range(t):
        n, a, b = test_cases[_]

        # Create a list of pairs (ai, bi, i) for both permutations
        pairs = [(a[i], b[i], i) for i in range(n)]

        # Sort the pairs based on the first element (ai)
        pairs.sort()

        # Create a mapping to keep track of the swaps
        swap_mapping = {i: i for i in range(n)}

        # Apply the swaps to minimize inversions
        for i, (_, _, original_index) in enumerate(pairs):
            a[original_index] = i + 1
            b[original_index] = swap_mapping[i] + 1

            # Update the swap mapping
            swap_mapping[i] = original_index

        results.append((a, b))

    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

# Get results
results = minimize_inversions(t, test_cases)

# Output the results
for result in results:
    print(" ".join(map(str, result[0])))
    print(" ".join(map(str, result[1])))
