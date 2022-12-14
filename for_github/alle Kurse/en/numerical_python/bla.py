import bk_random 

firstnames = ["Frank", "Eve", "Jane", "John", "Laura", "Robert", "Kathrin", "Roger", "Simone"]
surnames = ["Singer", "Miles", "Moore", "Looper", "Rampman", "Chopman", "Smiley"]
abbreviations = ["M.", "P.", "D. S.", "K.", "T."]
authors = set()
while len(authors) < 20:
    rlst = bk_random.random_list_from_iterables(firstnames, abbreviations, surnames)
    authors.add(" ".join(rlst))

print(authors)
