import math


class MyFirstClass(object):
    pass


class Point(object):

    def move(self, x, y):
        self.x = x
        self.y = y 

    def reset(self):
        self.move(1, 2)

    def calculate_distance(self, other_point):
        return math.sqrt(
                        (self.x - other_point.x) ** 2 +
                        (self.y - other_point.y) ** 2
                        )


class Point1(object):

    '''Represents the point in two dimentional co-ordinates.'''

    def __init__(self, x, y):
        '''Initialization of two dimentational co-ordinates.'''
        self.move(x, y)

    def move(self, x, y):
        '''Moving co-ordinates from one point to another point.'''
        self.x = x
        self.y = y     

    def reset(self):
        '''Resetting the co-ordinates value.'''
        self.move(0, 0)

    def calculate_distance(self, other_point):
        '''Distance calculation for co-ordination.'''
        return math.sqrt( (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 )


class SecretString(object):

    '''Secret string to store secure way!'''

    def __init__(self, plain_string, pass_phrase):
        '''Initialization of plain_string and pass_phrase for secret string.'''
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        '''Decrypting string with pass phrase.'''
        if pass_phrase == self.__pass_phrase:
             return self.__plain_string
        return ''
