import cv2 as cv
import numpy as np
from pathlib import Path


references = []

# Get the reference images
references_paths = Path("./references").glob("**/*.png")
for path in references_paths:
    references.append((str(path)[11], cv.imread(str(path))))


def get_wheel():
    # Get the image
    image = cv.imread("screen/10.png")
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
        _, thresh = cv.threshold(grey_image, 50, 255, cv.THRESH_BINARY)
    else:
        _, thresh = cv.threshold(grey_image, 50, 255, cv.THRESH_BINARY_INV)

    # Make a mask of everything but the wheel
    mask = np.zeros((height, width), dtype="uint8")
    cv.circle(mask, center, radius-10, 255, -1)
    letters = cv.bitwise_and(thresh, thresh, mask=mask)

    # Find contours
    contours, hierarchy = cv.findContours(letters, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Bounding rectangles
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        letter = letters[y: y + h, x: x + w]
        cv.imwrite(f"references/{x}.png", letter)


def get_letter(letter_image):
    min_error = -1
    min_error_letter = None
    for reference in references:
        resized = cv.resize(reference, letter_image.shape[:2])
        bin_xor = cv.binary_xor(reference, letter_image)
        cv.imwrite("images/binxor.png", bin_xor)
        count = np.sum(bin_xor > 0)
        print(count)

get_wheel()
