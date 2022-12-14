class Bruch(object):

    def __init__(self,z,n):
        self.__z = z
        self.__n = n
        self.kuerze()

    def __str__(self):
        return str(self.__z)+'/'+str(self.__n)

    @staticmethod
    def ggT(a,b):
        while b != 0:
            a,b = b,a%b
        return a

    def kuerze(self):
        g = self.ggT(self.__z, self.__n)
        self.__z = self.__z // g
        self.__n = self.__n // g

    def __mul__(self,other):
        p = Bruch(self.__z * other.__z,
                  self.__n * other.__n)
        p.kuerze()
        return p
    
    # in Python 2: __div__
    def __truediv__(self,other):
        p = Bruch(self.__z * other.__n,
                  self.__n * other.__z)
        p.kuerze()
        return p

    def __add(self, other):
        s = Bruch(self.__z*other.__n + other.__z * self.__n,
                     self.__n * other.__n)
        s.kuerze()
        return s

    def __add__(self, other):
        if type(other) == int:
            return self.__add(Bruch(other,1))
        elif type(other) == Bruch:
            return self.__add(other)
        else:
           return NotImplemented        

    def __radd__(self, other):
        if type(other) == int:
            return self.__add(Bruch(other,1))
        elif type(other) == Bruch:
            return other.__add(other)
        else:
           return NotImplemented

    def __sub__(self,other):
        s = Bruch(self.__z*other.__n - other.__z * self.__n,
                     self.__n * other.__n)
        s.kuerze()
        return s

    def __eq__(self, other):
        return self.__z * other.__n == other.__z * self.__n
    def __ne__(self, other):
        return not self.__eq__(other)
    def __gt__(self, other):
        return self.__z * other.__n > other.__z * self.__n
    def __ge__(self, other):
        return self.__z * other.__n >= other.__z * self.__n
    def __lt__(self, other):
        return self.__z * other.__n < other.__z * self.__n
    def __le__(self, other):
        return self.__z * other.__n <= other.__z * self.__n

if __name__ == "__main__":
    x = Bruch(2,6)
    y = Bruch(3,14)
    print(x * y)
    print(x / y)
    print(x + y)
    print(x - y)

    if x < y:
        print("x < y")
    else:
        print("x >= y")

    print(x)
