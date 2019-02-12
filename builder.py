"""Simplyfies building complex objects."""


class Director(object):

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engines()

    def get_car(self):
        return self._builder


class Builder(object):

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):

    def add_model(self):
        self.car.model = "SkyLark"

    def add_tires(self):
        self.car.tires = "Regular Tires"

    def add_engines(self):
        self.car.engines = "Two Stroke Engines"


class Car(object):

    def __init__(self):
        self.model = None
        self.tires = None
        self.engines = None

    def __str__(self):
        return f"{self.model} {self.tires} {self.engines}"


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)

