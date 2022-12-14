#roll dices
import random
import sys
while True:
    test_input=input("How many dice do you want to roll? (Please enter 1 to 6) ")
    print(test_input,type(test_input))
    try:
        number=int(test_input)     
    except:
        print("Bitte ganze Zahl zwischen 1 und 6 eingeben!")
        continue
    if 0<int(number)<=6:
        print("Eingabe ok")
        break
    else:
        print("Bitte ganze Zahl zwischen 1 und 6 eingeben!")
dice=[]           
for index in range(number-1):
    dice.append(random.randint(1,6))
print(dice)
tilde=chr(126)
tildes=(((15+(number-1)*12)-7)//2)
#print(tildes*tilde+"RESULTS"+tildes*tilde)


for line in range(15):
    print("   ",end="")
    for die in range(number):
        print(9*"#"+"   ",end="")
    print()
    
constr_dice=[["000","010","000"]]
line_l=[187,205,205,205,203,205,205,205,203,205,205,205,201]
for elem in line_l:
    print(chr(elem),end="")

print(chr(0x2588)) #0x2588
