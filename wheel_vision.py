import cv2 as cv
import numpy as np
import pytesseract
from rectangle import Rectangle


def GetWheel(imagePath: string, wheel_location: Rectangle):
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

    # Load in the image
    image = cv.imread(imagePath)
    hsv_image = cv.cvtColor(image, COLOR_BGR2HSV)


    # Sample a point on the wheel
    # The wheel can be black or white
    
        
