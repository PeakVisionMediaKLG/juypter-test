import matplotlib.pyplot as plt
import numpy as np

height, width = 2000, 3000
img = np.zeros((height, width, 3), dtype=np.uint8)  

for i in range(4):
    top_left = (np.random.randint(0, height), 
                np.random.randint(0, width))
    bottom_right = (np.random.randint(top_left[0], height), 
                    np.random.randint(top_left[1], width))             
    color = np.random.randint(0, 255, (3,))
    box = img[top_left[0]:bottom_right[0], 
              top_left[1]:bottom_right[1]]
    box[:] = color

#plt.axis('off')
plt.imshow(img, 
           cmap=plt.get_cmap("Spectral"), 
           interpolation='nearest')

plt.show()
