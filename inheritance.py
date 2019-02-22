""" Inheritance Exmaples."""


class Rectangle(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)


#class Square(object):
#
#    def __init__(self, length):
#        self.length = length
#
#    def area(self):
#        return 2 * self.length
#
#    def perimeter(self):
#        return 4 * self.length


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)
