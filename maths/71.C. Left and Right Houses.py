def solve(n, a):
    # Compute prefix sums for zeros and ones
    zeros_prefix_sum = [0] * (n + 1)
    ones_prefix_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        zeros_prefix_sum[i] = zeros_prefix_sum[i - 1] + (a[i - 1] == '0')
        ones_prefix_sum[i] = ones_prefix_sum[i - 1] + (a[i - 1] == '1')
    
    # Initialize variables to record the best position and its distance to the middle
    best_position = 0
    min_distance = float('inf')
    
    # Iterate through each possible position for the road
    for i in range(1,n + 1):
        # Calculate the number of satisfied residents on the left and right sides
        satisfied_left = zeros_prefix_sum[i]
        satisfied_right = ones_prefix_sum[n] - ones_prefix_sum[i]
        
        # Check if the conditions are satisfied for both sides
        if satisfied_left >= (i + 1) // 2 and satisfied_right >= (n - i + 1) // 2:
            # Calculate the distance to the middle
            distance = abs(n // 2 - i)
            
            # Update the best position if the current one is closer to the middle
            if distance < min_distance:
                min_distance = distance
                best_position = i
    
    return best_position

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input for each test case
    n = int(input())
    a = input()
    
    # Solve the problem and print the result for each test case
    print(solve(n, a))
