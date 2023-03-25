def distance(x1, y1, x2, y2):
    import math
    length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return length

x1, y1, x2, y2 = [float(input()) for i in range(4)]
print(distance(x1, y1, x2, y2))