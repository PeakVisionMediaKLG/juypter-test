import random
n = 20
to_be_guessed = random.randint(1,n)

guess = 0
while guess != to_be_guessed:
    guess = int(input("New guess: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Too large")
        elif guess < to_be_guessed:
            print("Too small")
    else:
        print("So, you are giving up!")
        break
else:
    print("Congratulation, you made it!")

