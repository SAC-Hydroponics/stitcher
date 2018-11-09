import cv2
import numpy as np
image1 = cv2.imread('oneaftertapemeasurer.png',0)
image2 = cv2.imread('3aftertapemeasurer.png',0)

rows,cols = image2.shape
y = int(25/(0.1388))

M = np.float32([[1,0,0],[0,1,-300]])
dst = cv2.warpAffine(image2,M,(cols,rows))

cv2.imshow('img',image1)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
