import math

def calculate_square_area(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    d2 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    d3 = math.sqrt((x3 - x4)**2 + (y3 - y4)**2)
    d4 = math.sqrt((x4 - x1)**2 + (y4 - y1)**2)


    side_length = min(d1, d2, d3, d4)


    return int(side_length**2)


t = int(input())

for _ in range(t):

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())


    print(calculate_square_area(x1, y1, x2, y2, x3, y3, x4, y4))


