"""Abstracte Factory."""


class Dog(object):

    def speak(self):
        return "Woooof"

    def __str__(self):
        return self.__class__.__name__


class DogFactory(object):

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food..!"


class PetStore(object):

    def __init__(self, pet_factory=None):
       self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print(f"Our pet is {pet}")
        print(f"Our pet food {pet_food}")


factory = DogFactory()
shop = PetStore(pet_factory=factory)
shop.show_pet()

