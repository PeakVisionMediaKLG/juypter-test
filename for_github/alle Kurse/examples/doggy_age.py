"""
Module with doggy functionalities .....
"""


def dog2human(age):
    """
    dog2human uses an integer 'age' as a parameter.
    This is the dog's age.
    The corresponding human age will be returned"""
    if age == 1:
        return 14
    elif age == 2:
        return 22
    else:
        return (age - 2) * 5 + 22


def check_age(s):
    """ The string 's' will be checked if it can be turned
    to in and that this in is a positive integer, i.e. a valid age"""
    try:
        x = int(s)
    except ValueError:
        return False
    return x > 0


def main_loop():
    """ Loop to calculate various Dog ages """
    while True:
        age_okay = False
        while not age_okay:
            age = input("Wie alt ist dein Hund? ")
            age_okay = check_age(age)
            if not age_okay:
                print("Probier's noch einmal!")
        age = int(age)
        print("Hund ist " + str(dog2human(age)) + " Jahre alt")
        cont = input("Weitermachen (J/N)? ")
        if cont.upper() == "N":
            print("Danke für Ihr Vertrauen!")
            break
