import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 177, 14 # mean and standard deviation
men = np.random.normal(mu, sigma, 20)
print(men)

mu, sigma = 167, 12
women = np.random.normal(mu, sigma, 20)
print(women)

cls = []
cls.append([ (train1[i], train2[i]) for i in range(len(train1)) if train1[i] < train2[i] ])
cls.append([ (train1[i], train2[i]) for i in range(len(train1)) if train1[i] >= train2[i] + waiting_time])
print(cls)


#n = np.random.normal(100*0.5, sqrt(100*0.5*0.5), size=10000)

#plt.hist(bi, bins=12, normed=True)
#plt.hist(n, alpha=0.5, bins=20, normed=True)


colours = ("r", "b")
for i in range(2):
    X, Y = zip(*cls[i])
    plt.scatter(X, Y, c=colours[i])

plt.show()
