n = int(input())
a = list(map(int,input().split()))

print(min(abs(i) for i in a))
