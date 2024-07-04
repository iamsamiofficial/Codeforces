def can_be_sorted_by_rotation(a):
    n = len(a)
    for i in range(n):
        rotated = a[i:] + a[:i]
        if rotated == sorted(a):
            return True
    return False


results = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if can_be_sorted_by_rotation(a):
        results.append("Yes")
    else:
        results.append("No")

# Output results
for result in results:
    print(result)
