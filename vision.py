import cv2 as cv
import numpy as np
import pytesseract


def get_wheel():
    # Get the image
    image = cv.imread("screen.png")
    height, width, channels = image.shape

    # Find the wheel
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(grey_image,cv.HOUGH_GRADIENT,2,200,
                              param1=200,param2=150,minRadius=width//5,maxRadius=width//3)


    circles = circles[0]
    circles = np.uint16(circles)

    # There should only be one circle
    assert len(circles) == 1

    circle = circles[0]
    center = (circle[0], circle[1])
    radius = circle[2]

    # Threshold the image
    if grey_image[circle[1], circle[0]] == 0:
        _, thresh = cv.threshold(grey_image, 250, 255, cv.THRESH_BINARY)
    else:
        _, thresh = cv.threshold(grey_image, 250, 255, cv.THRESH_BINARY_INV)

    # Make a mask of everything but the wheel
    mask = np.zeros((height, width), dtype="uint8")
    cv.circle(mask, center, radius - 5, 255, -1)
    letters = cv.bitwise_and(thresh, thresh, mask=mask)

    # Find contours
    contours, hierarchy = cv.findContours(letters, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Bounding rectangles
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
    cv.imwrite("images/bounding.png", image)

    cv.imwrite("images/mask-and-thresh.png", letters)

         
get_wheel()