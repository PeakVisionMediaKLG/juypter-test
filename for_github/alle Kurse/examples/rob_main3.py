from robots import Robot, NursingRobot, FightingRobot, FightingNurseRobot

x = FightingRobot("Rambo")

y = FightingRobot("Terminator")

x.say_hi()   # ---> Robot.say_hi(x)
y.say_hi()

x.attack(y)
print(x.healthy, y.healthy)

n = NursingRobot("Hubert")
n.say_hi()
n.say_hi_to_doc()

if not x.healthy:
    n.heal(x)
if not y.healthy:
    n.heal(y)


fn1 = FightingNurseRobot("Donald")
fn2 = FightingNurseRobot("Angela")

fn1.attack(fn2)
print(fn1.healthy, fn2.healthy)
fn1.heal(fn1)
fn2.heal(fn2)

"""
f1 = FightingRobot("Rambo")
f1.fight()
print(f1.healthy)
n.heal(f1)
"""
