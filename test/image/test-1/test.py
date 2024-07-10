import cv2 as cv
import numpy as np

path = "original.png"
image = cv.imread(path)

# Greyscale the image
grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imwrite("greyscale.png", grey)

# Threshold the image
t_, thresh = cv.threshold(grey, 250, 255, cv.THRESH_BINARY)
cv.imwrite("threshold.png", thresh)

# Find contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image, contours, -1, (0,255,0), 3)
cv.imwrite("contours.png", image)

# Bounding rectangles
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
cv.imwrite("bounding.png", image)

