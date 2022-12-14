from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS

from sklearn.neural_network import MLPClassifier
from sklearn import metrics


def text2paragraphs(filename, min_size=1):
    """ A text contained in the file 'filename' will be read 
    and chopped into paragraphs.
    Paragraphs with a string length less than min_size will be ignored.
    A list of paragraph strings will be returned"""
    
    txt = open(filename).read()
    paragraphs = [para for para in txt.split("\n\n") if len(para) > min_size]
    return paragraphs
    
    
labels = ['Virginia Woolf', 'Samuel Butler', 'Herman Melville', 
               'David Herbert Lawrence', 'Daniel Defoe', 'James Joyce']

files = ['to_the_lighthouse_woolf.txt', 'the_way_of_all_flash_butler.txt',
         'moby_dick_melville.txt', 'sons_and_lovers_lawrence.txt',
         'robinson_crusoe_defoe.txt', 'james_joyce_ulysses.txt']

path = "books/"

data = []
targets = []
counter = 0
for fname in files:
    paras = text2paragraphs(path + fname, min_size=150)
    data.extend(paras)
    targets += [counter] * len(paras)
    counter += 1
    
import random

data_targets = list(zip(data, targets))
# create random permuation on list:
data_targets = random.sample(data_targets, len(data_targets))

data, targets = list(zip(*data_targets))

from sklearn.model_selection import train_test_split

res = train_test_split(data, targets, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=42)
train_data, test_data, train_targets, test_targets = res 

vectorizer = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)
vectors = vectorizer.fit_transform(train_data)

print("creating a classifier")
classifier = MLPClassifier(random_state=1, max_iter=300).fit(vectors, train_targets)

print("classifier created")
vectors_test = vectorizer.transform(test_data)

predictions = classifier.predict(vectors_test)
accuracy_score = metrics.accuracy_score(test_targets, 
                                        predictions)
f1_score = metrics.f1_score(test_targets, 
                            predictions, 
                            average='macro')

print("accuracy score: ", accuracy_score)
print("F1-score: ", f1_score)
