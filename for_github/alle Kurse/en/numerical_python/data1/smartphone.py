fh = open("smartphone_vendors.txt")
fhw = open("new.txt", "w")

counter = 0
nline = ""
for line in fh:
    if len(line.strip()) <= 0:
         continue
    counter += 1
    nline += " " + line.rstrip()
    if counter == 5:
        fhw.write(nline + "\n")
        counter = 0
        nline = ""
        

fhw.close()
        
