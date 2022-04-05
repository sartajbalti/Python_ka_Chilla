from turtle import width
import cv2 as cv 
capture  = cv.VideoCapture(0)
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)
def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()