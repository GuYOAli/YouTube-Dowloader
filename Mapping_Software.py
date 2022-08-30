import math

# Random points

points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

newpoints = []

for (x, y) in points:
    result = math.sqrt((x ** 2) + (y ** 2))
    newpoints.append(result)

print("The fastest point to get to your destination is: ", min(newpoints))
