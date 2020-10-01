import numpy as np
import matplotlib.pyplot as plt

width  = 512
height = 512

#create an empty 2D matrix of type int
data = np.zeros( (512,512), dtype=np.uint8)

#put some data in some places
data[100:120, 100:120] = 1
data[100:120, 380:400] = 1
data[310:330, 150:350] = 1

#display data as an image
plt.imshow(data)

#show on the screen
plt.show()

