import numpy as np
import time

from collections import Counter

def find_interval(x, partition):
    """ find_interval -> i
        "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
        """
    
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1
    return -1



def weighted_choice(sequence, weights, bisection=False):
    """ 
    weighted_choice selects a random element of 
    the sequence according to the weights list
    """
    x = np.random.random()
    w = [0] + list(np.cumsum(weights))
    index = find_interval(x, w)
    return sequence[index]

def process_datafile(filename):
    """ process_datafile -> (universities, enrollments, total_number_of_students) 
        universities: list of University names
        enrollments: corresponding list with enrollments
        total_number_of_students: over all universities
    """

    universities = []
    enrollments = []
    with open(filename) as fh:
        total_number_of_students = 0
        fh.readline() # get rid of descriptive first line
        for line in fh:
             line = line.strip()
             *praefix, undergraduates, postgraduates, total = line.rsplit()
             university = praefix[1:]
             total = int(total.replace(",", ""))
             enrollments.append(total)
             universities.append(" ".join(university))
             total_number_of_students += total
    return (universities, enrollments, total_number_of_students)
        

universities, enrollments, total_students = process_datafile("universities_uk.txt")


normalized_enrollments = [ students / total_students for students in enrollments]


t1 = time.time()
outcomes = []
n = 2299380
for i in range(n):
    outcomes.append(weighted_choice(universities, normalized_enrollments, bisection=True))
print(time.time() - t1)

t1 = time.time()
outcomes = []
n = 2299380
for i in range(n):
    outcomes.append(weighted_choice(universities, normalized_enrollments, bisection=True))
print(time.time() - t1)

c = Counter(outcomes)
    
print(c.most_common(30))

