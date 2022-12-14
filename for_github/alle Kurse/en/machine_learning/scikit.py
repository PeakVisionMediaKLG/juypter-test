
# coding: utf-8

# ## Our Learning Set: "digits"

# In[33]:

get_ipython().magic('matplotlib inline')


# In[34]:

from sklearn import datasets
#iris = datasets.load_iris()
digits = datasets.load_digits()
print(type(digits))


# The digits dataset is a dictionary-like objects, containing the actual data and some metadata. 

# In[35]:

print(digits.data)


# In[ ]:




# digits.data contains the features, i.e. images of handwritten images of digits, which can be used for classification.

# In[36]:

digits.target


# In[37]:

len(digits.data), len(digits.target)


# digits.target contain the labels, i.e. digits from 0 to 9 for the digits of digits.data.
# The data "digits" is a 2 D array with the shape (number of samples, number of features). In our case, a sample is an image of shape (8, 8):

# In[38]:

print(digits.target[0], digits.data[0])
print(digits.images[0])


# ## Learning and Predicting

# We want to predict for a given image, which digit it depicts. Our data set contains samples
# for the classes 0 (zero) to 9 (nine). 
# We will use these samples to fit an estimator so that we can predict unseen samples as well.
# 
# In scikit-learn, an estimator for classification is a Python object that implements the methods fit(X,y) and
# predict(T).
# 
# An example of an estimator is the class sklearn.svm.SVC that implements support vector classification. The constructor of an estimator takes as arguments the parameters of the model, but for the time being, we will consider the estimator as a black box:

# In[39]:

from sklearn import svm            # import support vector machine
classifier = svm.SVC(gamma=0.001, C=100.)

classifier.fit(digits.data[:-3], digits.target[:-3])


# In[40]:

classifier.predict(digits.data[-3:])


# In[41]:

digits.target[-3:]


# In[42]:

digits.data[-3]


# In[43]:

from PIL import Image
img = Image.fromarray(digits.images[-1], 'RGB')
img.save('my.png')
img.show()


# In[ ]:




# In[ ]:



