# Resizing the Image

from cv2 import cvtColor
from matplotlib.image import imread
import numpy as np 
import cv2 as cv 

# Image Read 
img = cv.imread("D:/Git/first/OpenCV/resources/images/11.png")
img1 = cv.resize(img,(800,600))

#Display Code

cv.imshow("First Image", img1)

#Converting into Gray Scale
gimg = cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow("Second Image", gimg)

#Delay Code
cv.waitKey(0)
cv.destroyAllWindows()