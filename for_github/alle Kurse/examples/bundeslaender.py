
fh = open("bundeslaender.txt", encoding="ISO-8859-1")
#first line contains no data:
fh.readline()
max_size = 10000
small_lands = []
for line in fh:
    land, size_of_land, *rem = line.split()
    size_of_land = float(size_of_land)
    if size_of_land < max_size:
        small_lands.append(land)
print(small_lands)
        