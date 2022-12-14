class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x)
print(y)