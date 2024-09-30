class Shape():

    def area(self):
        return 0

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):

    def __init__(self, width, higth):
        self.witdh = width
        self.higth = higth

    def area(self):
        return self.witdh * self.higth

class Square(Shape):
    def __init__(self, width):
        self.witdh = width

    def area(self):
        return self.witdh ** 2

def print_area(shape):
    print(f"Площадь {shape.area()}")

circle = Circle(5)
square = Square(5)
rectangle = Rectangle(5,5)

print_area(circle)
print_area(square)
print_area(rectangle)

