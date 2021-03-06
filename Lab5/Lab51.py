import cv2 
import numpy as np
from scipy import ndimage
#Roberts Edge detection

img = cv2.imread("ball.jpg",0).astype('float64')
img/=255.0

robertsx = np.array( [[1, 0 ], [0,-1 ]] )
  
robertsy = np.array( [[ 0, 1 ], [ -1, 0 ]] )

vertical = ndimage.convolve( img, robertsx )
horizontal = ndimage.convolve( img, robertsy )
  
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255
cv2.imwrite("Roberts.jpg",edged_img)

