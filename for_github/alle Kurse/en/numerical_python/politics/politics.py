fh = open("wine.txt")

intros = []
for line in fh:
    if line.isupper():
        print(line.strip())


