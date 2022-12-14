# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 08:25:05 2017

@author: bernd
"""

def permutations(items):
    n = len(items)
    if n==0: 
        yield []
    else:
        for i, item in enumerate(items):
            for cc in permutations(items[:i] + items[i+1:]):
                yield [item] + cc


def combinations(items, k):
    if k==0: 
        yield []
    else:
        for item in items:
            for v in combinations(items, k-1):
                if item not in v:
                    yield [item] + v

for combination in combinations(["a", "b", "c", "d", "e"], 3):
    print(combinations)

print("""permutations for (['r','e','d']""")
for p in permutations(['r','e','d']): 
    print(''.join(p))

print("""permutations of the letters of the string "bin" """)
for p in permutations(list("bin")): 
    print(''.join(p))
    
