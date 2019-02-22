import copy


class Prototype(object):

    def __init__(self):
        self._object = {}

    def register_obj(self, name, obj):
        self._object[name] = obj

    def unregister_obj(self, name):
        del self._object[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._object.get(name)
        obj.__dict__.update(attr)
        return obj


class Car(object):

    def __init__(self):
        self.name = "SkyLark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name} {self.color} {self.options}"


c = Car()
prototype = Prototype()
prototype.register_obj("skylark", c)
c1 = prototype.clone()
print(c1)

