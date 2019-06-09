import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generate some sample data

lena = cv2.imread('../../SampleImages/lenna.png',0)


# downscaling has a "smoothing" effect
lena = cv2.resize(lena, (100,100))

# create the x and y coordinate arrays (here we just use pixel indices)
xx, yy = np.mgrid[0:lena.shape[0], 0:lena.shape[1]]

# create the figure
fig = plt.figure()
ax = fig.gca(projection='3d')

#
# #For Colormap - Jet
#
# ax.plot_surface(xx, yy, lena ,rstride=1, cstride=1, cmap=plt.cm.jet,
#                 linewidth=0)

#
# #For Colormap - Grayscale
#
ax.plot_surface(xx, yy, lena ,rstride=1, cstride=1, cmap=plt.cm.gray,
                linewidth=0)

# show it
plt.show()