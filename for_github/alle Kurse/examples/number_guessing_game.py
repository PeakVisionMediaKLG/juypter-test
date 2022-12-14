import random
n = 20
to_be_guessed = random.randint(1,n)
guess = 0
while guess != to_be_guessed:
    if guess > 0:
        if guess > to_be_guessed:
            print("Number is too large")
        else:
            print("Number is too small")
    guess = int(input("New guess: "))
print("You got it!")

