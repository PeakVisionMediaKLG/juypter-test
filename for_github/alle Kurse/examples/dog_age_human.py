age = int(input("Alter des Hundes: "))
# Python2:
# age = int(raw_input("Dog's age: "))
print()
if age < 1:
    print("Das kann wohl nicht stimmen!")
elif age == 1:
    print("entspricht 14 Jahren")
elif age == 2:
    print("entsprich 22 Jahren")
elif age > 2:
    human = 22 + (age -2)*5
    print("Menschenjahre:", human)

### 
# Python 2:
# raw_input('press Return>')
input('press Return>')

