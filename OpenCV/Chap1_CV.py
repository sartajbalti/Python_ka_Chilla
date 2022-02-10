from matplotlib.image import imread
import numpy as np 
import cv2 as cv 

img = cv.imread("resources/images/11.png")
cv.imshow("First Image", img)

cv.waitKey(0)


