import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def longest_special_subsequence(n, arr):
    arr_set = set(arr)
    max_length = 0
    
    # Initialize dp table with 0s
    dp = [0] * (n + 1)
    
    # Iterate over all elements in the array
    for i in range(n):
        # Iterate over all elements before the current element
        for j in range(i):
            # If arr[i] is divisible by arr[j]
            if arr[i] % arr[j] == 0:
                # Calculate the LCM of arr[i] and arr[j]
                subsequence_lcm = lcm(arr[i], arr[j])
                # If the LCM is not in the array, update dp[i] with max value
                if subsequence_lcm not in arr_set:
                    dp[i] = max(dp[i], dp[j] + 1)
        # Update max_length with the maximum value found
        max_length = max(max_length, dp[i])
    
    return max_length

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Compute and print the length of the longest special subsequence
    print(longest_special_subsequence(n, arr))
