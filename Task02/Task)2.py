from point2D import Point2D
from manager import Manager

p1 = Point2D()
p2 = Point2D(3, 4)

print(p1)
print(p2)

distance = Manager.calculate_distance(p2, p1)

print(f"Distance between points is {distance}.")