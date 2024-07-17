from pathlib import Path
import numpy as np
import cv2 as cv

import config


references = []

# Get the reference images
references_paths = Path("./references").glob("**/*.png")
for path in references_paths:
    references.append((str(path)[11], cv.imread(str(path),
                                                cv.IMREAD_GRAYSCALE)))


def get_wheel():
    # We will return a list of dict, the first being the letter,
    # then the location
    wheel = dict()

    # Get the image
    image = cv.imread("screen/screen.png")
    height, width, channels = image.shape

    # Find the wheel
    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(grey_image, cv.HOUGH_GRADIENT, 2, 200,
                              param1=200, param2=150, minRadius=width//5,
                              maxRadius=width//3)

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
    contours, hierarchy = cv.findContours(letters, cv.RETR_EXTERNAL,
                                          cv.CHAIN_APPROX_SIMPLE)

    # Bounding rectangles
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        letter = letters[y: y + h, x: x + w]
        x_position = ((x + w/2)/width)*config.phone_width
        y_position = ((y + h/2)/height)*config.phone_height
        wheel[get_letter(letter)] = (x_position, y_position)

    return wheel


def get_letter(letter_image):
    min_error = letter_image.size + 1
    min_error_letter = None
    for reference in references:
        resized = cv.resize(reference[1], tuple(letter_image.shape[1::-1]))
        bit_xor = cv.bitwise_xor(resized, letter_image)
        count = cv.countNonZero(bit_xor)
        if count < min_error:
            min_error = count
            min_error_letter = reference[0]
    return min_error_letter


print(get_wheel())
