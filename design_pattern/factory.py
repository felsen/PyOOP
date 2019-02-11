"""Factory is an object, which creates other object."""


class Dog(object):

    """Dog class have name, and language."""

    def __init__(self, name):
        """Initiating dog name."""
        self._name = name

    def speak(self):
        """Returning dog language."""
        return "Woooof"

    def __call__(self):
        """Returning the speech."""
        return self.speak()

    def __str__(self):
        """String representation of an object."""
        return self.__class__.__name__


class Cat(object):

    """Cat have name, and language."""

    def __init__(self, name):
        """Initiating cat name."""
        self._name = name

    def speak(self):
        """Returning cat language."""
        return "Meoooov"
    
    def __call__(self):
        """Returning the speech."""
        return self.speak()

    def __str__(self):
        """String representation of an object."""
        return self.__class__.__name__


def get_pet(pet="dog"):

    """Returning pet object."""

    pets = {"dog": Dog("steve"), "cat": Cat("felix")}
    return pets[pet]

