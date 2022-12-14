
# coding: utf-8

# ## Our Learning Set: "digits"

# In[ ]:




# ## Instance Based Learning -- -k-nearest-neighbor
# 
# Instance based learning works directly on the learned samples, instead of creating rules compared to other classification methods.
# 
# Way of working: Each new instance is compared with the already existing instances. The instances are compared by using a distance metric. The instance with the closest distance value detwermines the class for the new instance. This classification method is called nearest-neighbor classification. 
# 
# ### k-nearest-neighbor from Scratch

# In[18]:


# In[19]:


import numpy as np
from sklearn import datasets
from collections import Counter

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
print(iris_X[:8])


# We create a learnset from the sets above. We use permutation from np.random to split the data randomly:

# In[20]:

np.random.seed(42)
indices = np.random.permutation(len(iris_X))
n_training_samples = 12
iris_X_train = iris_X[indices[:-n_training_samples]]
iris_y_train = iris_y[indices[:-n_training_samples]]
iris_X_test = iris_X[indices[-n_training_samples:]]
iris_y_test = iris_y[indices[-n_training_samples:]]
print(iris_X_test)


# To determine the similarity between to instances, we need a distance function. In our example, the Euclidean distance is ideal:

# In[21]:

def distance(instance1, instance2):
    # just in case, if the instances are lists or tuples:
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)



# In[24]:

def get_neighbors(training_set, 
                  labels, 
                  test_instance, 
                  k, 
                  distance=distance):
    distances = []
    for index in range(len(training_set)):
        dist = distance(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors

def vote(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    return class_counter.most_common(1)[0][0]

def vote_prob(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    return winner, votes4winner/sum(votes)
  
def vote_weighted(neighbors):
    class_counter = Counter()
    for index in range(len(neighbors)):
        class_counter[neighbors[index][2]] += 1/(index+1)
    labels, votes = zip(*class_counter.most_common())
    #print(labels, votes)
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    return winner, votes4winner / sum(votes)

train_set = [(1, 2, 2), 
             (-3, -2, 0),
             (1, 1, 3), 
             (-3, -3, -1),
             (-3, -2, -0.5),
             (0, 0.3, 0.8),
             (-0.5, 0.6, 0.7),
             (0, 0, 0)
            ]

labels = ['apple',  'banana', 'apple', 
          'banana', 'apple', "orange",
          'orange', 'orange']

k = 1
for test_instance in [(0, 0, 0), (2, 2, 2), 
                      (-3, -1, 0), (0, 1, 0.9),
                      (1, 1.5, 1.8), (0.9, 0.8, 1.6)]:
    neighbors = get_neighbors(train_set, 
                              labels, 
                              test_instance, 
                              2)
    #print("vote: ", vote(neighbors))
    #print("vote_prob: ", vote_prob(neighbors))
    print("vote_weighted: ", vote_weighted(neighbors))
    #print(test_instance, neighbors)


# In[ ]:




# ### Example: Levenstein

# In[26]:

from levenshtein import levenshtein

cities = []
with open("data/city_names.txt") as fh:
    for line in fh:
        city = line.strip()
        if " " in city:
            # like Freiburg im Breisgau add city only as well
            cities.append(city.split()[0])
        cities.append(city)

#cities = cities[:20]

for city in ["Freiburg", "Frieburg", "Freiborg", "Hamborg"]:
    print(city)
    neighbors = get_neighbors(cities, 
                              cities, 
                              city, 
                              2,
                              distance=levenshtein)
    """

    print("vote_weighted: ", vote_weighted(neighbors))
    """

# In[ ]:




# In[ ]:



