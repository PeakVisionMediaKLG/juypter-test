"""
The Robot module, implementing ...."""


class Robot:
    """ The Robot class ...."""

    __forbidden_names = {"Henry", "Oscar", "Theo"}

    def __init__(self, name, city="Hamburg"):
        self.set_name(name)
        self.city = city

    def say_hi(self):
        print("Hi, I am " + self.get_name() + " from " + self.city)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name in Robot.__forbidden_names:
            raise ValueError("Kein erlaubter Name")
        else:
            self.__name = name

    def __add__(self, other):
        return Robot(self.get_name() + "-" + other.get_name(), "Berlin")
    