import numpy as np
import matplotlib.pyplot as plt


train1 = np.random.binomial(n=22, p=0.5, size=35)
train2 = np.random.binomial(n=8, p=0.8, size=35)

waiting_time = 5
cls = []
cls.append([ (train1[i], train2[i]) for i in range(len(train1)) if train1[i] < train2[i] + waiting_time ])
cls.append([ (train1[i], train2[i]) for i in range(len(train1)) if train1[i] >= train2[i] + waiting_time])


#n = np.random.normal(100*0.5, sqrt(100*0.5*0.5), size=10000)

#plt.hist(bi, bins=12, normed=True)
#plt.hist(n, alpha=0.5, bins=20, normed=True)


colours = ("r", "g")
for i in range(2):
    X, Y = zip(*cls[i])
    print(cls[i])

    plt.scatter(X, Y, c=colours[i])

plt.show()
