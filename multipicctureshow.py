#Import modules
import cv2
import numpy as np

#import images
image1 = cv2.imread('oneaftertapemeasurer.png',0)
image2 = cv2.imread('3aftertapemeasurer.png',0)


#Translate 2nd image
rows,cols = image2.shape
y = int(25/(0.1388))
M = np.float32([[1,0,0],[0,1,-y]])
dst = cv2.warpAffine(image2,M,(cols,rows))

#Add images together
result = cv2.add(image1, dst)
#result = image1 + dst

width, height = result.shape
print('width = ' + str(width))
print('height = ' + str(height))

#Display result
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
