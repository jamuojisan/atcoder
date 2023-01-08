import math
a, b, d= map(int, input().split())
rad = math.radians(d)
x = math.cos(rad)*a - math.sin(rad)*b
y = math.cos(rad)*b + math.sin(rad)*a
print(x, y)
