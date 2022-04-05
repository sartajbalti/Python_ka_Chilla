from matplotlib.image import imread
import numpy as np 
import cv2 as cv 

img = cv.imread("resources/images/11.png")
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)
cv.imshow("First Image", img)

cv.waitKey(0)


