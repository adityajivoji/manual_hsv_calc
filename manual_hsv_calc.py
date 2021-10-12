import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0 + cv.CAP_DSHOW)
key = 0
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
img = np.zeros((300,512,3), np.uint8)
kernel = np.ones((3, 3), np.uint8)
# create trackbars for color change
cv.createTrackbar('LH','image',0,179,nothing)
cv.createTrackbar('LS','image',0,255,nothing)
cv.createTrackbar('LV','image',0,255,nothing)
cv.createTrackbar('UH','image',0,179,nothing)
cv.createTrackbar('US','image',0,255,nothing)
cv.createTrackbar('UV','image',0,255,nothing)
while key != 27:
    ret, fram = cap.read()
    cv.imshow('image',img)
    frame = cv.cvtColor(fram,cv.COLOR_BGR2HSV)
    LH = cv.getTrackbarPos('LH','image')
    LS = cv.getTrackbarPos('LS','image')
    LV = cv.getTrackbarPos('LV','image')
    UH = cv.getTrackbarPos('UH','image')
    US = cv.getTrackbarPos('US','image')
    UV = cv.getTrackbarPos('UV','image')
    lower = np.array([LH,LS,LV])
    upper = np.array([UH,US,UV])
    mask = cv.inRange(frame, lower, upper)
    res = cv.bitwise_and(fram,fram, mask= mask)
    cv.imshow("res",res)
    cv.imshow("mask",mask)
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    dilation_after_closing = cv.dilate(closing,kernel,iterations = 3)
    key = cv.waitKey(1)
cap.release()
cv.destroyAllWindows()
