import cv2
import imutils
import numpy as np

img = cv2.imread(r"./geometric.jpg")

rot = imutils.rotate(img, angle=-15)

width, height = 806, 429

# pixel points of 4 corners
pts1 = np.float32([[110,0],[494,102],[0,413],[384,517]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
result = cv2.warpPerspective(rot,matrix,(width,height))

cv2.imshow("img", img)
cv2.imshow("rot", rot)
cv2.imwrite('result.jpg', result)

cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
