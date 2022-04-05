#  Draw lines text on image 
import cv2 as cv 
import numpy as np 
blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)
# # Paint the image with certain color
# blank[:] = 0,225,0
# cv.imshow('Green',blank)
# blank[:] = 225,0,0
# cv.imshow('Blue',blank)
# blank[200:300,300:400] = 0,0,225
# cv.imshow('Red in Blue',blank)
# Draw a rectangle 
cv.rectangle(blank,(0,0),(250,250),(0,225,0), thickness=-1)
#cv.imshow('Rectangle',blank)
# Draw a circle 
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
#cv.imshow('Circle',blank)
# Draw a line 
cv.line(blank,(0,0),(250,250),(225,225,225), thickness=4)
#cv.imshow('line',blank)
#write text on image 
cv.putText(blank, "Open-CV Practice", (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(122,133,122),2)
cv.imshow('Text',blank)
cv.waitKey(0)