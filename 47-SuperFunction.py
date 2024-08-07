# Super() = function used to give access to the methods of a parent class.
#           Return a tempory object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(2,2)
cube = Cube(5,7,8)
print(square.area())
print(cube.volume())

