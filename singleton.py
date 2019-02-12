class Borg(object):

   _shared_state = {}

   def __init__(self, **kwargs):
        self.__dict__ = self._shared_state


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)

x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)
y = Singleton(SNMP="Simple Network Mail Protocol")
print(y)

