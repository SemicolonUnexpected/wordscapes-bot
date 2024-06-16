import cv2 as cv


def main():
    print("----- Wordscapes Bot ------");

    cam = cv.VideoCapture(0)
    ret, frame = cam.read()
    print(type(frame))



if __name__ == "__main__":
    main()    
