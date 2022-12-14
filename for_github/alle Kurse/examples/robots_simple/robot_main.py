from robots import Robot

x = Robot("Marvin")
print("Name von x", x.get_name())
x.say_hi()     # ---> Robot.say_hi(x)

y = Robot("Laila", "Berlin")

y.say_hi()
y.set_name("Theodophyla")
z = x + y
z.say_hi()
