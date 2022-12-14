import os
from glob import glob
import re


path = "/home/bernd/dropbox/websites/python-course.eu/books/"
os.chdir(path)
words_novels = {}
all_words = set()
for fname in glob("*.txt"):
    if fname != "words_only_in_ulysses.txt":
        txt = open(fname).read().lower()
        words = re.findall(r"[\w-]+", txt)
        print(f"{fname:22s}:\n{len(words):7d}, {len(set(words)):7d}")
        words_novels[fname] = set(words)
        all_words = all_words.union(words_novels[fname])

print(len(all_words))

cut_set = words_novels["james_joyce_ulysses.txt"].copy()
for fname in words_novels:
    if fname != "words_only_in_ulysses.txt" and\
             fname != "james_joyce_ulysses.txt":
        cut_set &= words_novels[fname]

print(len(cut_set))

joyce_words = words_novels["james_joyce_ulysses.txt"]
print("Joyce words: ", len(joyce_words))
for fname in words_novels:
    if fname != "words_only_in_ulysses.txt" and\
             fname != "james_joyce_ulysses.txt":
        print(fname)
        joyce_words -= words_novels[fname]
        print(len(joyce_words))
