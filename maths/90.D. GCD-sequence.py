# from math import gcd

# def is_non_decreasing(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
#     return True

# def check_gcd_sequence(n, arr):
#     gcd_seq = []
#     for i in range(n - 1):
#         gcd_seq.append(gcd(arr[i], arr[i + 1]))

#     if is_non_decreasing(gcd_seq):
#         return "YES"

#     for i in range(n - 1):
#         temp_arr = arr[:i] + arr[i + 1:]
#         temp_gcd_seq = [gcd(temp_arr[i], temp_arr[i + 1]) for i in range(len(temp_arr) - 1)]
#         if is_non_decreasing(temp_gcd_seq):
#             return "YES"

#     return "NO"

# # Input
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     # Output
#     print(check_gcd_sequence(n, arr))


def check(i,l):
    store = []
    g = []
    for j in range(len(l)):
        if i!=j:
            store.append(l[j])
    for i in range(len(store)-1):
        g.append(math.gcd(store[i],store[i+1]))
    if g == sorted(g):
        return True
    else:
        False 


def calculate(n,l):
    a = []
    for i in range(n-1):
        a.append(math.gcd(l[i],l[i+1]))
    
    if a == sorted(a):
        return True
    else:
        for i in range(n-1):
            if a[i]>a[i+1]:
                d = check(i,l)
                if d:
                    return True
                e = check(i+1,l)
                if e:
                    return True
                f = check(i+2,l)
                if f:
                    return True
                else:
                    return False



import math
def main():
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().split()))
        b = calculate(n,l)
        if b:
            print("YES")
        else:
            print("NO")
main()




        



    