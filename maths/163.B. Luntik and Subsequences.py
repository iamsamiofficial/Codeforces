for _ in range(int(input())):
    n = int(input())
    s = input().split()
    print((1<<s.count("0"))*s.count("1"))
    