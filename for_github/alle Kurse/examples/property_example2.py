class P:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """Docstring 'x'"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
    
p = P
p.x = 42
print(p.x)