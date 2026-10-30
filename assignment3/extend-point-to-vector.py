# Task 5

import math     

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y # the statement itself is True or False
    
    def distance(self, other):
        result1, result2 = self.x - other.x , self.y - other.y
        return math.hypot(result1, result2) # distance formula shortcut

class Vector(Point): # Parenthesis let Vector inherit the methods from Point

    def __str__(self):
        return f"Vector <{self.x},{self.y}>"
    
    def __add__(self, other):
        result1, result2 = self.x + other.x , self.y + other.y
        return Vector(result1,result2)

if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    print(p1)
    print(p2)

    print(p1 == p2)
    print(Point(0, 0).distance(Point(3, 4)))   # 5.0

    v1 = Vector(12, 24)
    v2 = Vector(3, 4)
    print(v1)
    print(v2)

    print(v1 + v2)      # Vector<15, 28>
    print(v1 == v2)     # False, using Point's __eq__, inherited
    print(v1.distance(v2))