import cv2 as cv
import numpy as np
import pytesseract


def get_wheel():
    # Get the image
    image = cv.imread("screen.png")
    height, width, channels = image.shape

    # Find the wheel
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray_image,cv.HOUGH_GRADIENT,2,200,
                              param1=200,param2=150,minRadius=width//5,maxRadius=width//3)


    # Create an image with the wheel circle drawn on to 
    circles = np.uint16(circles)
    for i in circles[0, :]:
        center = (i[0], i[1])
        # Circle center
        cv.circle(image, center, 2, (0, 0, 255), 3)
        # Circle outline
        radius = i[2]
        cv.circle(image, center, radius, (255, 0, 255), 3)

    cv.imwrite("circled.png", image)

    # Sample the center point on the wheel
    # The wheel can be black or white
         
