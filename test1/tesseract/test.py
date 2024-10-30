import pytesseract
import cv2 as cv

image = cv.imread("test2.jpeg")
grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(grey, lang='eng', config='--psm 10')
# text = pytesseract.image_to_string(grey, lang='eng', config='--psm 10 -c load_system_dawg=false -c load_freq_dawg=false -c 0tessedit_char_whitelist=0123456789r°:-abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(text)
