import random

class Robot:

    def __init__(self, name):
        self.name = name  #---> property setter
        self.healthy = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "Henry":
            self.__name = "Marvin"
        else:
            self.__name = name

    def __str__(self):
        return self.name + ", Robot"

    def __add__(self, other):
        return Robot(self.name + "-" + other.name)

    def say_hi(self):
        print("Hi, I am " + self.name)



class NursingRobot(Robot):

    def say_hi(self):
        print("Well, well, everything will be fine ... " + self.name + " takes care of you!")

    def heal(self, robo):
        robo.healthy = True
        print(robo.name + " is healed now!")
        

class FightingRobot(Robot):

    def say_hi(self):
        print("I am the terrible ... " + self.name + " and soon you will be ...!")

    def fight(self):
        self.healthy = random.choice([False, True])


x = NursingRobot("Robert")
x.say_hi()
NursingRobot.say_hi(x)
Robot.say_hi(x)

y = FightingRobot("Rambo")
y.say_hi()
y.fight()

if not y.healthy:
    x.heal(y)
print(y.healthy)





