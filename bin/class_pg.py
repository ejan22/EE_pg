
# reference:   https://realpython.com/python-super/
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
    def area(self):
        print('in Square area')
        return super().area()


class Cube(Square):
    def __init__(self, length):
        super().__init__(length)

    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super(Square, self).__init__(base, base)
        super().__init__(base, slant_height)

    def area(self):
        base_area = super(Square, self).area()
        perimeter = super(Square, self).perimeter()
        triangle_area = super().area()
        # triangle_area = 1
        print (f'base={base_area},  perimeter={perimeter}, triangle_area={triangle_area}')
        return triangle_area * 4 + base_area


