import random

min_number = 1
max_number = 100

to_be_guessed = random.randint(min_number, 
                               max_number)

illogical = 0

curses = [["Zahl nicht im Bereich", "Zahl ist zu klein oder zu groß"],
          ["Verstehst du nicht die Regeln!", "Lies mal die Regeln", "RTFM!"],
          ["Ich glaube das wird wohl nichts mit uns!", "Klappt wohl nicht"],
          ["Willst du mich ärgern?", "Du willst mich wohl provozieren..."],
          ["Bald habe ich keine Lust mehr!"]]
guess = int(input("Dein Versuch: "))
while guess != to_be_guessed:
    if guess < min_number or guess > max_number:
        if illogical < len(curses):
            level_list = curses[illogical]
            curse = random.choice(level_list)
            print(curse)
        else:
            print("Jetzt reicht's aber ...")
            break
        illogical += 1
    elif guess > to_be_guessed:
        max_number = guess - 1
        print("zu groß!")
    else:
        min_number = guess + 1
        print("zu klein")
    guess = int(input("Noch ein Versuch: "))

if illogical == len(curses):
    print("Mit dir spiel' ich nicht mehr!")
else:
    print("Jawohl, das war's! Glückwunsch!")
        