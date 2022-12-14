data = []
fh = open("hacker_poll.txt")
for line in fh:
    language, votes = line.strip().rsplit(None, 1)
    data.append((language, int(votes)))

data.sort(key=lambda x: (x[1], x[0]), reverse = True)

top10 = data[:10]
print(top10)
