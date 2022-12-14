import re

path = "autonummern"
no_of_files = 5

def get_licence_numbers(filename):
    txt = open(filename, encoding="iso-8859-1").read()
    licence_numbers = re.findall(r"\b[A-Z]{1,3}\s[A-Z]{1,2}\s[0-9]{1,4}\b", txt)
    return set(licence_numbers)

checkpoints = []
for num in range(1, no_of_files+1):
    fname = "autonummern" + str(num) + ".txt"
    print(fname)
    checkpoints.append(get_licence_numbers(path + "/" + fname))

suspects = checkpoints[0] 
for i in range(1, no_of_files):
     suspects &= checkpoints[i]
print(suspects)
