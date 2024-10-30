import cv2 as cv
import numpy as np
import pytesseract
from rectangle import Rectangle


def GetWheel(image: str, wheel_location: Rectangle):
    """ This method takes in the image of the phone screen
    and returns the each character, and its position on the wheel
        
        Parameters
        ----------
        image: numpy.ndarray
            The image of the wordscapes screen
        wheel_location: Rectangle
            The rectangle, in pixels, which encompasses the wheel

        Returns
        -------
        List
            The list of characters and corresponding locations
    """

    # Find the wheel
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray_image,cv.HOUGH_GRADIENT,2,200,
                              param1=200,param2=200,minRadius=300,maxRadius=700)

    print(circles)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(image, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(image, center, radius, (255, 0, 255), 3)

    cv.imwrite("test.png", image)

    # Sample a point on the wheel
    # The wheel can be black or white
    
        

image = cv.imread("./../image/test-2/original-2.jpg")
GetWheel(image, None)
