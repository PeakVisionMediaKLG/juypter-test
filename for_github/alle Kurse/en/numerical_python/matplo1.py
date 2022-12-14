import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

X = np.arange(0,10)
Y = np.random.randint(1,20, size=10)
left, bottom, width, height = 0.2, 0.2, 0.7, .6
axes = fig.add_axes([left, bottom, width, height])

axes.plot(X, Y, 'g')
plt.show(fig)

