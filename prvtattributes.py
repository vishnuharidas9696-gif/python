class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()

r1 = Rectangle(8, 6)
r2 = Rectangle(8, 6)

if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller or equal area")
